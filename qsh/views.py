from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse

from .models import Shoplist, Buyable, Buydetail, User
from .forms import BuydetailForm

def index(request):
    return HttpResponse("halo")

def _shoplist_add_buydetail(shoplist, buyable, quantity):
    buydetail = Buydetail()
    buydetail.shoplist = shoplist
    buydetail.buyable = buyable
    buydetail.quantity = quantity
    buydetail.save()

def shoplist_add_new(request, shoplist_id):

    shoplist = Shoplist.objects.get(pk=shoplist_id)

    if request.method == 'POST':
        form = BuydetailForm(request.POST)
        if form.is_valid():

            buyable_name = form.cleaned_data['name']

            # don't create another if name already exists
            buyable_lookup = Buyable.objects.filter(name=buyable_name, user=shoplist.user)
            if buyable_lookup:
                buyable = buyable_lookup
            else:
                buyable = Buyable()
                buyable.name = buyable_name
                buyable.user = shoplist.user
                buyable.save()

            _shoplist_add_buydetail(shoplist, buyable, form.cleaned_data['quantity'])

            return HttpResponseRedirect(reverse('qsh:shoplist_edit', args=(shoplist.id,)))

    form = BuydetailForm()

    return render(request, 'qsh/shoplist_add_new.html', { 'shoplist': shoplist, 'form': form })

def shoplist_add_many(request, shoplist_id):

    shoplist = Shoplist.objects.get(pk=shoplist_id)

    if request.method == 'POST':
        buyables_to_add = request.POST.getlist('buyables_to_add')

        for buyable_id in buyables_to_add:
            buyable = Buyable.objects.get(pk=buyable_id)
            _shoplist_add_buydetail(shoplist, buyable, 1)

        return HttpResponseRedirect(reverse('qsh:shoplist_edit', args=(shoplist.id,)))

    buyables_all = Buyable.objects.all()
    buydetails_in_shoplist = shoplist.buydetail_set.all()
    buyables = []
    for buyable in buyables_all:
        is_in_shoplist = False
        for buydetail in buydetails_in_shoplist:
            if buydetail.buyable.id == buyable.id:
                is_in_shoplist = True
        if not is_in_shoplist:
            buyables.append(buyable)

    return render(request,
        'qsh/shoplist_add_many.html', {
            'shoplist': shoplist,
            'buyables': buyables,
            })

def shoplist_edit(request, shoplist_id):

    shoplist = Shoplist.objects.get(pk=shoplist_id)

    if request.method == 'POST':
        buydetails_to_delete = request.POST.getlist('buydetails_to_delete')

        for buydetail_id in buydetails_to_delete:
            buydetail = Buydetail.objects.get(pk=buydetail_id)
            buydetail.delete()

    return render(request, 'qsh/shoplist_edit.html', { 'shoplist': shoplist })

class ShoplistsView(generic.ListView):
    model = Shoplist
    def get_queryset(self):
        # TODO filter by user
        return Shoplist.objects.all()

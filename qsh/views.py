from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Shoplist, Buyable, Buydetail, User
from .forms import BuydetailForm, ShoplistForm

@login_required
def shoplist_add_new(request, shoplist_id):
    shoplist = Shoplist.get_one(shoplist_id, request.user)
    if request.method == 'POST':
        form = BuydetailForm(request.POST)
        if form.is_valid():
            buyable_name = form.cleaned_data['name']
            buyable = Buyable.fetch_or_create(name=buyable_name, user=request.user)
            shoplist.add_buydetail(buyable, form.cleaned_data['quantity'])
            return HttpResponseRedirect(reverse('qsh:shoplist_edit', args=(shoplist.id,)))
    form = BuydetailForm()
    return render(request, 'qsh/shoplist_add_new.html', { 'shoplist': shoplist, 'form': form })

@login_required
def shoplist_add_many(request, shoplist_id):
    shoplist = Shoplist.get_one(shoplist_id, request.user)
    if request.method == 'POST':
        buyables_to_add = request.POST.getlist('buyables_to_add')
        for buyable_id in buyables_to_add:
            buyable = Buyable.objects.get(pk=buyable_id)
            shoplist.add_buydetail(buyable, 1)
        return HttpResponseRedirect(reverse('qsh:shoplist_edit', args=(shoplist.id,)))

    buyables = shoplist.get_unused_buyables()
    return render(request,
        'qsh/shoplist_add_many.html', {
            'shoplist': shoplist,
            'buyables': buyables,
            })

@login_required
def shoplist_edit(request, shoplist_id):
    shoplist = Shoplist.get_one(shoplist_id, request.user)
    if request.method == 'POST':
        buydetails_to_delete = request.POST.getlist('buydetails_to_delete')
        for buydetail_id in buydetails_to_delete:
            buydetail = Buydetail.objects.filter(pk=buydetail_id, shoplist=shoplist)
            buydetail.delete()
    return render(request, 'qsh/shoplist_edit.html', { 'shoplist': shoplist })

@login_required
def shoplist_create(request):
    if request.method == 'POST':
        form = ShoplistForm(request.POST)
        if form.is_valid():
            shoplist_name = form.cleaned_data['name']
            # TODO error message for same name
            Shoplist.save_new(shoplist_name, request.user)
            return HttpResponseRedirect(reverse('qsh:shoplist_edit', args=(shoplist.id,)))
    form = ShoplistForm()

    return render(request, 'qsh/shoplist_create.html', { 'form': form })

@login_required
def shoplist_delete(request):
    if request.method == 'POST':
        shoplists_to_delete = request.POST.getlist('shoplists_to_delete')

        for shoplist_id in shoplists_to_delete:
            shoplist = Shoplist.get_one(shoplist_id, request.user)
            for buydetail in Buydetail.objects.filter(shoplist=shoplist):
                buydetail.delete()
            shoplist.delete()

    return HttpResponseRedirect(reverse('qsh:shoplist_list'))

class ShoplistsView(LoginRequiredMixin, generic.ListView):
    model = Shoplist
    def get_queryset(self):
        # TODO filter by user
        return Shoplist.objects.filter(user=self.request.user)

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse

from .models import Shoplist, Buyable, Buydetail, User
from .forms import BuydetailForm

def index(request):
    return HttpResponse("halo")

def shoplist_add_many(request, shoplist_id):
    return HttpResponse("shoplist_add_many %s" % shoplist_id)

def shoplist_add_new(request, shoplist_id):

    shoplist = Shoplist.objects.get(pk=shoplist_id)

    if request.method == 'POST':
        form = BuydetailForm(request.POST)
        if form.is_valid():
            buyable = Buyable()
            buyable.name = form.cleaned_data['name']
            buyable.user = shoplist.user
            buyable.save()

            buydetail = Buydetail()
            buydetail.shoplist = shoplist
            buydetail.buyable = buyable
            buydetail.quantity = form.cleaned_data['quantity']
            buydetail.save()

            return HttpResponseRedirect(reverse('qsh:shoplist_edit', args=(shoplist_id,)))
    else:
        form = BuydetailForm()

    return render(request, 'qsh/shoplist_add_new.html', { 'shoplist': shoplist, 'form': form })

class ShoplistsView(generic.ListView):
    model = Shoplist
    def get_queryset(self):
        # TODO filter by user
        return Shoplist.objects.all()

class ShoplistEdit(generic.DetailView):
    model = Shoplist
    template_name = 'qsh/shoplist_edit.html'

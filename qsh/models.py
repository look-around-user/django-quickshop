from django.db import models
from django.contrib.auth.models import User

class Shoplist(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    @staticmethod
    def get_one(pk, user):
        for shoplist in Shoplist.objects.filter(pk=pk, user=user):
            return shoplist
        return None

    @staticmethod
    def save_new(name, user):
        shoplist = Shoplist()
        shoplist.name = name
        shoplist.user = user
        shoplist.save()
        return shoplist

    def add_buydetail(self, buyable, quantity):
        buydetail = Buydetail()
        buydetail.shoplist = self
        buydetail.buyable = buyable
        buydetail.quantity = quantity
        buydetail.save()

    def get_unused_buyables(self):
        buyables_all = Buyable.objects.filter(user=self.user)
        buydetails_in_shoplist = self.buydetail_set.all()
        buyables = []
        for buyable in buyables_all:
            is_in_shoplist = False
            for buydetail in buydetails_in_shoplist:
                if buydetail.buyable.id == buyable.id:
                    is_in_shoplist = True
            if not is_in_shoplist:
                buyables.append(buyable)
        return buyables

class Buyable(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #last_use = models.DateField()
    def __str__(self):
        return self.name

    @staticmethod
    def save_new(name, user):
        buyable = Buyable()
        buyable.name = name
        buyable.user = user
        buyable.save()
        return buyable

    @staticmethod
    def fetch_or_create(name, user):
        buyable_lookup = Buyable.objects.filter(name=name, user=user)
        if buyable_lookup:
            buyable = buyable_lookup
        else:
            buyable = Buyable.save_new(name, user)
        return buyable

class Buydetail(models.Model):
    shoplist = models.ForeignKey(Shoplist, on_delete=models.CASCADE)
    buyable = models.ForeignKey(Buyable, on_delete=models.CASCADE)
    quantity = models.IntegerField();
    #note = models.CharField(max_length=50)
    def __str__(self):
        return self.buyable.name

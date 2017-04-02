from django.contrib import admin

# Register your models here.
from .models import Shoplist, Buyable, Buydetail, User

admin.site.register(User)
admin.site.register(Shoplist)
admin.site.register(Buyable)
admin.site.register(Buydetail)

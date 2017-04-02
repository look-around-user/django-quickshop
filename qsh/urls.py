from django.conf.urls import url

from . import views

app_name = 'qsh'
urlpatterns = [
    url(r'^$', views.ShoplistsView.as_view(), name='shoplist_list'),
    url(r'^(?P<pk>[0-9]+)/edit$', views.ShoplistEdit.as_view(), name='shoplist_edit'),
    url(r'^(?P<shoplist_id>[0-9]+)/addMany$', views.shoplist_add_many, name='shoplist_add_many'),
    url(r'^(?P<shoplist_id>[0-9]+)/addNew$',  views.shoplist_add_new,  name='shoplist_add_new'),
#    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
]

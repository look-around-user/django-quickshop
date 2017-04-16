from django.conf.urls import url

from . import views

app_name = 'qsh'
urlpatterns = [
    url(r'^$', views.ShoplistsView.as_view(), name='shoplist_list'),
    url(r'^list_all/json$', views.shoplist_list_all_json, name='shoplist_list_all_json'),
    url(r'^create$', views.shoplist_create, name='shoplist_create'),
    url(r'^create_modal$', views.shoplist_create_modal, name='shoplist_create_modal'),
    url(r'^delete$', views.shoplist_delete, name='shoplist_delete'),
    url(r'^(?P<shoplist_id>[0-9]+)/edit$', views.shoplist_edit, name='shoplist_edit'),
    url(r'^(?P<shoplist_id>[0-9]+)/addNew$', views.shoplist_add_new, name='shoplist_add_new'),
    url(r'^(?P<shoplist_id>[0-9]+)/addMany$', views.shoplist_add_many, name='shoplist_add_many'),
    #    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
]

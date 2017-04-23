from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'shoplists', views.ShoplistViewSet)
router.register(r'buyables', views.BuyableViewSet)
router.register(r'buydetails', views.BuydetailViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^rest/', include('rest_framework.urls', namespace='rest_framework')),
]

from rest_framework import viewsets
from qsh.models import Shoplist, Buyable, Buydetail
from .serializers import ShoplistSerializer, BuyableSerializer, BuydetailSerializer


class ShoplistViewSet(viewsets.ModelViewSet):
    queryset = Shoplist.objects.all()
    serializer_class = ShoplistSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class BuyableViewSet(viewsets.ModelViewSet):
    queryset = Buyable.objects.all()
    serializer_class = BuyableSerializer


class BuydetailViewSet(viewsets.ModelViewSet):
    queryset = Buydetail.objects.all()
    serializer_class = BuydetailSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

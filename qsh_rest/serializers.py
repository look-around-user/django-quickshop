from rest_framework import serializers
from qsh.models import Shoplist, Buyable, Buydetail
from django.contrib.auth.models import User


class ShoplistSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Shoplist
        fields = ('url', 'id', 'name', 'owner')


class BuyableSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Buyable
        fields = ('url', 'id', 'name', 'owner')


class BuydetailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Buydetail
        fields = ('shoplist', 'buyable', 'quantity')

from rest_framework import serializers, viewsets
from .models import MenuItem, MeatItem


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('__all__')


class MeatItemSerializer(MenuItemSerializer):
    class Meta:
        model = MeatItem
        fields = ('__all__')


class MenuItemViewSet(viewsets.ModelViewSet):
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()


class MeatItemViewSet(MenuItemViewSet):
    serializer_class = MeatItemSerializer
    queryset = MeatItem.objects.all()

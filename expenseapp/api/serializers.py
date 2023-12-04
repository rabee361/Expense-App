from rest_framework.serializers import ModelSerializer
from expenseapp.models import *

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


# class 
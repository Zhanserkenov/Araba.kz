# serializers.py
from rest_framework import serializers
from .models import Car, Charging, Article


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class ChargingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charging
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
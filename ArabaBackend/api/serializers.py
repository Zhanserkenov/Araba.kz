from api.models import Category, Car, Like, Accessory, ChargingStation, Article
from rest_framework import serializers


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def create(self, validated_data):
        category = Category.objects.create(**validated_data)
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Like
        fields = ('id', 'car', 'user')


class CarSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Car
        fields = ('id', 'name', 'description', 'category_id', 'price', 'img', 'liked')
        read_only_fields = ('id',)

    def create(self, validated_data):
        category_id = validated_data.pop('category_id', None)
        if category_id is not None:
            validated_data['category'] = Category.objects.get(id=category_id)
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        category_id = validated_data.pop('category_id', None)
        if category_id is not None:
            validated_data['category'] = Category.objects.get(id=category_id)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class AccessorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessory
        fields = '__all__'

    def create(self, validated_data):
        return Accessory.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.brand = validated_data.get('brand', instance.brand)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance


class ChargingStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargingStation
        fields = '__all__'

    def create(self, validated_data):
        return ChargingStation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.make = validated_data.get('make', instance.make)
        instance.model = validated_data.get('model', instance.model)
        instance.charging_time = validated_data.get('charging_time', instance.charging_time)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.save()
        return instance

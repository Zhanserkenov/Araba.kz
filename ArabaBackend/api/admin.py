from django.contrib import admin

from api.models import Category

from api.models import Car, Like, Article, Accessory, ChargingStation


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'make', 'model', 'description', 'category')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'car', 'user')


@admin.register(Accessory)
class AccessoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'price')


@admin.register(ChargingStation)
class ChargingStationAdmin(admin.ModelAdmin):
    list_display = ('id', 'make', 'model', 'charging_time', 'price')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'published_date')

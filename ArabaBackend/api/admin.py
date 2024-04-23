from django.contrib import admin

from api.models import Category

from api.models import Car, Like


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'make', 'model', 'description', 'category')


@admin.register(Like)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'car', 'user')

from django.contrib import admin

from arababack.models import Car, Charging, Article

# Register your models here.
admin.site.register(Car)
admin.site.register(Charging)
admin.site.register(Article)
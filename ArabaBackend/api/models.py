from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255)  # by default not null

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def __str__(self):
        return f'{self.id}: {self.name}'


class Car(models.Model):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    description = models.TextField()

    # this will writen as category_id in database
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='cars')

    price = models.IntegerField()
    img = models.TextField()
    liked = models.BooleanField()

    #   TextField, CharField -> while creating if we not provide  by default it will be empty string

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'category_id': self.category.id,
            'price': self.price,
            'img': self.img,
            'liked': self.liked
        }

    def __str__(self):
        return f'{self.id}: {self.name} , {self.description}, {self.category}'


"""
Rules:
1) The Category column of car table can not be null(one car -> one category)
"""


class Like(models.Model):
    car = models.ForeignKey(Car,
                                 on_delete=models.CASCADE,
                                 related_name='likes',
                                )
    user = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                             related_name='likes')

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'


class Accessory(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'brand': self.brand,
            'price': str(self.price),
        }

    def __str__(self):
        return f'{self.id}: {self.name} ({self.brand})'

class ChargingStation(models.Model):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    charging_time = models.DurationField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def to_json(self):
        return {
            'id': self.id,
            'make': self.make,
            'model': self.model,
            'charging_time': str(self.charging_time),
            'price': str(self.price),
        }

    def __str__(self):
        return f'{self.id}: {self.make} {self.model}'

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateField()

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'published_date': self.published_date.strftime('%Y-%m-%d')
        }

    def __str__(self):
        return f'{self.id}: {self.title}, published on {self.published_date}'

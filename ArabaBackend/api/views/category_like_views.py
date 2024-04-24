from rest_framework import generics
from api.models import Category, Like, Car
from api.serializers import CategorySerializer, LikeSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.db.models import Subquery, OuterRef
from django.forms.models import model_to_dict


class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    lookup_url_kwarg = 'category_id'
    queryset = Category.objects.all()


class LikeAPIView(generics.ListCreateAPIView):  # post and get
    serializer_class = LikeSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        likes = Like.objects.filter(user=self.request.user)
        cars = Car.objects.filter(id__in=Subquery(likes.values('car')))
        for car in cars:
            if Like.objects.filter(car=car).exists():
                car.liked = True
        cars_list = [model_to_dict(car) for car in cars]
        return JsonResponse(cars_list, safe=False)

    def post(self, request, *args, **kwargs):
        try:
            print('nice')
            car = Car.objects.get(pk=request.data.get('car'))
            user = self.request.user
            like = Like.objects.get(car=car, user=user)
            like.delete()
            return JsonResponse({'message': 'Deleted like from database.'})
        except Like.DoesNotExist:
            print('nice')
            car = Car.objects.get(pk=request.data.get('car'))
            user = self.request.user
            Like.objects.create(car=car, user=user)
            return JsonResponse({'message': 'Added like to database.'})


class LikeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LikeSerializer
    permission_classes = (IsAuthenticated,)
    lookup_url_kwarg = 'like_id'

    def get_queryset(self):
        return Like.objects.filter(user=self.request.user)

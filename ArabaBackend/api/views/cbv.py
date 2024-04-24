from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.models import Category, Like
from api.serializers import CategorySerializer


class CategoryListAPIView(APIView):
    authentication_classes = [JWTAuthentication]  # Добавлено
    permission_classes = [IsAuthenticated]  # Добавлено

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Изменено
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryCarListAPIView(APIView):
    authentication_classes = [JWTAuthentication]  # Добавлено
    permission_classes = [IsAuthenticated]  # Добавлено

    def get_object(self, category_id):
        try:
            return Category.objects.get(pk=category_id)
        except Category.DoesNotExist as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, category_id):
        category = self.get_object(category_id)
        cars = category.cars.all()
        for car in cars:
            if Like.objects.filter(car=car).exists():
                car.liked = True
        cars_list = [model_to_dict(car) for car in cars]
        print(cars_list)
        return JsonResponse(cars_list, safe=False)

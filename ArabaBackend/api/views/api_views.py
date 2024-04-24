import json

from django.forms import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from api.models import Car, Category, Like

# CRUD - CRATE, READ, UPDATE, DELETE
from api.serializers import CategorySerializer, CarSerializer


@csrf_exempt
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = CategorySerializer(instance=category, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({'deleted': True})


@csrf_exempt
def car_list(request):
    if request.method == 'GET':
        title = request.GET.get('title')
        if title:
            cars = Car.objects.filter(name__icontains=title)
            print(cars)
        else:
            cars = Car.objects.all()
        for car in cars:
            if Like.objects.filter(car=car).exists():
                car.liked = True
        cars_list = [model_to_dict(car) for car in cars]
        return JsonResponse(cars_list, safe=False)

    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = CarSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def car_detail(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    if request.method == 'GET':
        serializer = CarSerializer(car)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = CarSerializer(instance=car, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        car.delete()
        return JsonResponse({'deleted': True})

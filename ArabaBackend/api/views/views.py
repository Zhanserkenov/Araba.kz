import json
from api.models import Category, Car, Accessory, Article, ChargingStation
from django.http.response import JsonResponse
from django.contrib.auth.models import User

# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from api.serializers import AccessorySerializer, ChargingStationSerializer, ArticleSerializer


@csrf_exempt
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        categories_json = [c.to_json() for c in categories]
        return JsonResponse(categories_json, safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        category_name = data.get('name', '')
        category = Category.objects.create(name=category_name)
        return JsonResponse(category.to_json())


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    user = request.user
    data = {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
    }
    return JsonResponse(data)


@csrf_exempt
def registration(request):
    data = json.loads(request.body)
    user = User.objects.create_user(username=data.get('username'), password=data.get('password'))
    user.first_name = data.get('first_name')
    user.last_name = data.get('last_name')
    user.save()
    return JsonResponse({"user_name": user.first_name})


@csrf_exempt
def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    if request.method == 'GET':
        return JsonResponse(category.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        new_category_name = data.get('name', category.name)
        category.name = new_category_name
        category.save()
        return JsonResponse(category.to_json())
    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({'deleted': True})


@csrf_exempt
def car_list(request):
    if request.method == 'GET':
        cars = Car.objects.all()
        cars_json = [p.to_json() for p in cars]
        return JsonResponse(cars_json, safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        car_make = data.get('make', '')
        car_model = data.get('model', '')
        car_description = data.get('description', '')
        # assume that only existing category will be matched
        car_category_id = data.get('category_id')
        car_price = data.get('price', 0)
        car_image = data.get('img', '')
        car_liked = data.get('liked', False)
        car_category = Category.objects.get(id=car_category_id)

        car = Car.objects.create(
            img=car_image,
            description=car_description,
            make=car_make,
            model=car_model,
            price=car_price,
            liked=car_liked,
            category=car_category
        )
        return JsonResponse(car.to_json())


@csrf_exempt
def car_detail(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    if request.method == 'GET':
        return JsonResponse(car.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        car_make = data.get('make', car.make)
        car_model = data.get('model', car.model)
        car_description = data.get('description', car.description)
        car_price = data.get('price', car.price)
        car_image = data.get('img', car.img)
        car_liked = data.get('liked', car.liked)
        car_category_id = data.get('category_id', car.category.id)
        car_category = Category.objects.get(id=car_category_id)
        car.make = car_make
        car.model = car_model
        car.description = car_description
        car.price = car_price
        car.img = car_image
        car.liked = car_liked
        car.category = car_category
        car.save()
        return JsonResponse(car.to_json())
    elif request.method == 'DELETE':
        car.delete()
        return JsonResponse({'deleted': True})


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def accessory_list(request):
    if request.method == 'GET':
        accessories = Accessory.objects.all()
        serializer = AccessorySerializer(accessories, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)
    elif request.method == 'POST':
        serializer = AccessorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201, safe=False)
        return JsonResponse(serializer.errors, status=400, safe=False)


def charging_station_list(request):
    if request.method == 'GET':
        stations = ChargingStation.objects.all()
        serializer = ChargingStationSerializer(stations, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)
    elif request.method == 'POST':
        serializer = ChargingStationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201, safe=False)
        return JsonResponse(serializer.errors, status=400, safe=False)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201, safe=False)
        return JsonResponse(serializer.errors, status=400, safe=False)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return JsonResponse({'message': 'Article not found'}, status=404, safe=False)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data, status=200, safe=False)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200, safe=False)
        return JsonResponse(serializer.errors, status=400, safe=False)
    elif request.method == 'DELETE':
        article.delete()
        return JsonResponse({'deleted': True}, status=204, safe=False)

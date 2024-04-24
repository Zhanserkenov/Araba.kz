import json
from api.models import Accessory, Article, ChargingStation
from django.http.response import JsonResponse
from django.contrib.auth.models import User

# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from api.serializers import ArticleSerializer, ChargingStationSerializer, AccessorySerializer


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

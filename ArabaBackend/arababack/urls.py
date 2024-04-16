# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, ChargingViewSet, ArticleViewSet

router = DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'article', ArticleViewSet)
router.register(r'charging', ChargingViewSet)
urlpatterns = [
    path('', include(router.urls)),
]

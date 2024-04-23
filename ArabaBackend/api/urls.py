from api import views
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
   path('cars/', views.car_list),
   path('cars/<int:car_id>/', views.car_detail),
   path('categories/', views.CategoryListAPIView.as_view()),
   path('categories/<int:category_id>/', views.CategoryDetailAPIView.as_view()),
   path('categories/<int:category_id>/cars/', views.CategoryCarListAPIView.as_view()),
   path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('registration/', views.registration),
   path('user/', views.get_user),
   path('likes/', views.LikeAPIView.as_view()),
   path('likes/<int:like_id>/', views.LikeDetailAPIView.as_view())
]

from .views import registration, get_user
from .category_like_views import CategoryDetailAPIView, CategoryListAPIView, LikeAPIView, LikeDetailAPIView
from .api_views import category_list, category_detail, car_list, car_detail
from .cbv import CategoryCarListAPIView
from .views import accessory_list, charging_station_list, article_list, article_detail
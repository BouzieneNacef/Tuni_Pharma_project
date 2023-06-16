from django.urls import path, include, re_path
from . import views
from.views import MyTokenObtainPairView
from rest_framework import routers
from .viewSets import *
from .views import*

# get instance of the router defined in rest_framework
router = routers.DefaultRouter()
#add Product and client urls( get, post, put, delete) 
router.register(r'product', ProductViewSet, basename='product') 
router.register(r'client', ClientViewSet, basename='clent')
router.register(r'command',CommandViewSet,basename='command')
router.register(r'details',CommandDetailsViewSet,basename='command_details')
router.register(r'category',CategoryViewSet,basename='product_category')
router.register(r'pannier',PannierViewSet,basename='pannier')
router.register(r'delivery',DeliveryInformationViewSet,basename='delivery')

 
from rest_framework_simplejwt.views import (
    TokenRefreshView,                                                                           
)

urlpatterns = [
path('', include(router.urls)),
path('base/', views.getRoutes),
path('auth/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
path(r'product/add', views.add_product),
path(r'product/all', views.get_all_product),
path(r'product/', views.filter_products_by_name),
path(r'product/<int:id>', views.retreive_update_or_delete_product),
path(r'command/add', views.add_command),
path(r'command/<int:id>', views.retreive_update_or_delete_command),
path(r'client/add', views.add_client),
path(r'client/<int:id>', views.retreive_update_or_delete_client),
path(r'details/add', views.add_details),
path(r'details/<int:id>', views.retreive_update_or_delete_details),
path(r'delivery/add', views.add_delivery),
path(r'delivery/<int:id>', views.retreive_update_or_delete_delivery),
path(r'pannier/add', views.add_pannier),
path(r'pannier/<int:id>', views.retreive_update_or_delete_pannier),
path(r'category/add', views.add_category),
path(r'category/<int:id>', views.retreive_update_or_delete_category),



#path('product/', views.product_crud, name="product"),


 ]


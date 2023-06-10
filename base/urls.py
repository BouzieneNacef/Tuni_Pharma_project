from django.urls import path, include, re_path
from . import views
from.views import MyTokenObtainPairView
from rest_framework import routers
from .viewSets import *

# get instance of the router defined in rest_framework
router = routers.DefaultRouter()
# add Product and client urls( get, post, put, delete) 
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
path(r'product/<int:id>', views.retreive_update_or_delete_product),

#path('product/', views.product_crud, name="product"),


 ]


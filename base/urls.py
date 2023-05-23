from django.urls import path, include
from . import views
from.views import MyTokenObtainPairView
from rest_framework import routers
from .viewSets import *

router = routers.DefaultRouter()   #get the default router object defined in rest_framework
router.register(r'product_viewSet', ProductViewSet) 

 
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


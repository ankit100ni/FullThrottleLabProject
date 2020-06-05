from django.contrib import admin
from rest_framework import routers
from . import views
from django.urls import include, path


router = routers.DefaultRouter()
router.register(r'UserDF', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
from django.urls import path, include
from django.conf.urls import url

from api.views.auth_views import UserViewSet, AuthViewSet
from rest_framework import renderers
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'auth', AuthViewSet, base_name='Auth')
router.register(r'users', UserViewSet, base_name='User')

urlpatterns = [
    url(r'', include(router.urls)),
]

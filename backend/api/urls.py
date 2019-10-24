from django.urls import path
from .views.views import *
from api.views.auth_views import RegistrationAPI, LoginAPI, UserAPI

urlpatterns = [
    path("auth/register/", RegistrationAPI.as_view()),
    path("auth/login/", LoginAPI.as_view()),
    path("auth/user/", UserAPI.as_view()),
    path('site/list/', APIListView.as_view()),
    path('site/detail/<int:obj_pk>', APIDetailView.as_view()),
]

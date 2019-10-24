from django.urls import path

from .views.site_views import *
from .views.rating_views import *

from .views.views import *
from api.views.auth_views import RegistrationAPI, LoginAPI, UserAPI

urlpatterns = [
    path("auth/register/", RegistrationAPI.as_view()),
    path("auth/login/", LoginAPI.as_view()),
    path("auth/user/", UserAPI.as_view()),
    path('site/list/', APIListView.as_view()),
    path('site/detail/<int:site_pk>', APIDetailView.as_view()),
    path('rating/list/', RatingView.as_view()),
    path('rating/edit/<int:rating_pk>', RatingEditView.as_view()),
]

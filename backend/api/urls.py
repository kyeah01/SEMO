from django.contrib import admin
from django.urls import path
from .views.site_views import *
from .views.rating_views import *

urlpatterns = [
    path('site/list/', APIListView.as_view()),
    path('site/detail/<int:site_pk>', APIDetailView.as_view()),
    path('rating/list/', RatingView.as_view()),
    path('rating/edit/<int:rating_pk>', RatingEditView.as_view()),
]

from django.contrib import admin
from django.urls import path
from .views.views import *

urlpatterns = [
    path('site/list/', APIListView.as_view()),
]

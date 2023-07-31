from django.urls import path
from . import views

urlpatterns = [
    path("", views.xmas, name='index')
]

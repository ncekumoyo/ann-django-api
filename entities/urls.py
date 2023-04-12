from django.urls import path
from . import views

urlpatterns = [
    path('', views.EntityListCreateView.as_view()),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.AnnListCreateView.as_view()),
]

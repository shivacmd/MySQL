from django.urls import path 
from .views import ListCityAPIView, ListStateAPIView


urlpatterns = [
     path('cities/', ListCityAPIView.as_view()),
     path('states/',ListStateAPIView.as_view())
]

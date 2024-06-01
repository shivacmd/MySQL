from django.urls import path 
from .views import ListCreateCategoryAPIView, MainSearchAPIView


urlpatterns = [
     path('categories/', ListCreateCategoryAPIView.as_view()),
     path('properties/', MainSearchAPIView.as_view())
]

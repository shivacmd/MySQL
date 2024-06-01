from core.models import City , State
from rest_framework import generics
from .serializer import CitySerializer , StateSerializer

class ListCityAPIView(generics.ListAPIView):
    queryset = City.objects.filter(is_active=True)
    serializer_class = CitySerializer


class ListStateAPIView(generics.ListAPIView):
    queryset = State  .objects.filter(is_active=True)
    serializer_class = StateSerializer
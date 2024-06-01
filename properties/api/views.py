from rest_framework import generics
from properties.models import Category
from .serializers import CategorySerializer, MainSearchSerializer, BuidingSerializer
from rest_framework.views import APIView 
from properties.models import Building, BuildingAddress
from rest_framework.response import Response
from rest_framework import status
from core.models import City


class ListCreateCategoryAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer


class MainSearchAPIView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = MainSearchSerializer(data=request.data)
        if serializer.is_valid():
            category_id = serializer.validated_data['category_id']
            city_id = serializer.validated_data['city_id']
            try:
                city = City.objects.get(id=city_id)
            except City.DoesNotExist:
                return Response('Invalid City ID', status=status.HTTP_404_NOT_FOUND)
            buildings = Building.objects.filter(buildingaddress__city=city, is_active=True, categories__in=[category_id])
            building_serializer = BuidingSerializer(buildings, context={'request': request}, many=True,)
            return Response(building_serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


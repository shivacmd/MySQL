from rest_framework import serializers
from properties.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ('id', 'name', 'logo')

    def to_representation(self, instance):
        data = super().to_representation(instance=instance)
        request = self.context.get('request')
        if request:
            image_url = instance.logo.url
            absolute_url = request.build_absolute_uri(image_url)
            data['logo'] = absolute_url
        else:
            data['logo'] = None
        return data

class BuildingInfoSerializser(serializers.ModelSerializer):
    class Meta:
        model = BuildingInfo
        fields = ('id', 'name')



class BuildingInfoValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingInfoValue
        fields = ('id', 'name')
        
    def to_representation(self, instance):
        data = super().to_representation(instance=instance)
        building_info_serialization = BuildingInfoSerializser(instance.building_info)
        data['info'] = building_info_serialization.data
        return data


class BuildingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingDetail
        fields = ['id']

    def to_representation(self, instance):
        data = super().to_representation(instance=instance)
        building_info_value_serrialization = BuildingInfoValueSerializer(instance.building_info_value)
        data['info_value'] = building_info_value_serrialization.data
        return data
        


class BuidingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        exclude = ('is_active', 'created_at', 'updated_at', 'categories')
        
    def to_representation(self, instance):
        data = super().to_representation(instance=instance)
        request = self.context.get('request')
        amenity_serialization = AmenitySerializer(instance.amenities.all(), many=True, context={'request': request})
        


        building_details = BuildingDetail.objects.filter(building=instance)
        building_detail_serialization = BuildingDetailSerializer(building_details, context={'request': request}, many=True)
        building_image_serialization = BuildingImageSerializser(instance.building_images.all(), many=True, context={'request': request})

        data['amenities'] = amenity_serialization.data
        data['datails'] = building_detail_serialization.data
        data['images'] = building_image_serialization.data
        return data 
        


class BuildingImageSerializser(serializers.ModelSerializer):
    class Meta:
        model = BuildingImage
        fields = ('id', 'image', 'is_primary')

    def to_representation(self, instance):
        data = super().to_representation(instance=instance)
        request = self.context.get('request')
        if request:
            image_url = instance.image.url
            absolute_url = request.build_absolute_uri(image_url)
        else:
            data['image'] = None
        return data






class OwnerContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerContact
        fields = '__all__'


class MainSearchSerializer(serializers.Serializer):
    """
    Search by category and City
    """
    category_id = serializers.IntegerField()
    city_id = serializers.IntegerField()



from django.db import models
from core.models import TimestampModel, State, City
from core.common import MOBILE_REGEX

class Category(TimestampModel):
    name = models.CharField(max_length=150, unique=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    

class Collection(TimestampModel):
    name = models.CharField(max_length=150, unique=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Amenity(TimestampModel):
    name = models.CharField(max_length=150, unique=True)
    logo = models.ImageField(upload_to='amenities/', max_length=100)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Amenities' 

    def __str__(self):
        return self.name

class Building(TimestampModel):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
    amenities = models.ManyToManyField(Amenity)
    coordinate = models.CharField(max_length=300)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
    
    

class BuildingInfo(TimestampModel):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'Building Information'

    def __str__(self):
        return self.name 


class BuildingInfoValue(TimestampModel):
    building_info = models.ForeignKey(BuildingInfo, on_delete=models.CASCADE, related_name='build_info_values')
    name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.building_info.name} -> {self.name}'

class BuildingDetail(TimestampModel):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='buildings')
    building_info_value = models.ForeignKey(BuildingInfoValue, on_delete=models.CASCADE, related_name='build_details')
    
    def __str__(self):
        return self.building.name


class BuildingImage(TimestampModel):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='building_images')
    image = models.ImageField(upload_to='building/pics', height_field=None, width_field=None, max_length=None)
    is_primary = models.BooleanField(default=False)
    
    def __str__(self):
        return self.building.name
    
    
class BuildingAddress(TimestampModel):
    building = models.OneToOneField(Building, on_delete=models.CASCADE)
    address_line1 = models.CharField(max_length=50)
    address_line2 = models.CharField(max_length=50, null=True, blank=True)
    area = models.CharField(max_length=150)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='adresses')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='addresses')

    class Meta:
        verbose_name_plural = 'Building Addresses' 

    def __str__(self):
        return self.building.name

class OwnerContact(TimestampModel):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='owner_contacts')
    name = models.CharField(max_length=150)
    contact = models.CharField(max_length=10, validators=[MOBILE_REGEX])
    
    def __str__(self):
        return self.name
    
    


    
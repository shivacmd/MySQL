# Generated by Django 5.0.5 on 2024-05-16 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_alter_amenity_options_alter_buildingaddress_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='amenity',
            name='logo',
            field=models.ImageField(default=1, upload_to='amenities/'),
            preserve_default=False,
        ),
    ]
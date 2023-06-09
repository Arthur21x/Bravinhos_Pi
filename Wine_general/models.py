from django.db import models


# Create your models here.

class WineData(models.Model):
    data_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=32)
    description = models.TextField(max_length=255)
    designation = models.CharField(max_length=64)
    points = models.IntegerField()
    price = models.FloatField()
    province = models.CharField(max_length=32)
    region_1 = models.CharField(max_length=32)
    region_2 = models.CharField(max_length=32)
    variety = models.CharField(max_length=32)
    winery = models.CharField(max_length=32)


class WineDetails(models.Model):
    detail_id = models.AutoField(primary_key=True)
    fixed_acidity = models.FloatField()
    volatile_acidity = models.FloatField()
    citric_acid = models.FloatField()
    residual_sugar = models.FloatField()
    chlorides = models.FloatField()
    free_sulfur_dioxide = models.FloatField()
    total_sulfur_dioxide = models.FloatField()
    density = models.FloatField()
    ph = models.FloatField()
    sulphates = models.FloatField()
    alcohol = models.FloatField()
    quality = models.IntegerField()

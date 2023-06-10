from django.db import models


# Create your models here.

class WineData(models.Model):
    data_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=32, blank=True)
    description = models.TextField(max_length=255)
    designation = models.CharField(max_length=64, blank=True)
    points = models.IntegerField(blank=True, default=0)
    price = models.FloatField(blank=True, default=0)
    province = models.CharField(max_length=32, blank=True)
    region_1 = models.CharField(max_length=32, blank=True)
    region_2 = models.CharField(max_length=32, blank=True)
    variety = models.CharField(max_length=32, blank=True)
    winery = models.CharField(max_length=32, blank=True)


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

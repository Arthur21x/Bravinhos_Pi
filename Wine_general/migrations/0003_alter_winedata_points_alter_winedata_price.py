# Generated by Django 4.2.1 on 2023-06-10 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wine_general', '0002_alter_winedata_country_alter_winedata_designation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='winedata',
            name='points',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='winedata',
            name='price',
            field=models.FloatField(blank=True, default=0),
        ),
    ]

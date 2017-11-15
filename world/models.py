from django.contrib.gis.db import models


class WorldBorder(models.Model):
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS code', max_length=2)
    iso2 = models.CharField('2 digit ISO', max_length=2)
    iso3 = models.CharField('3 digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()
    mpoly = models.MultiPolygonField()

    def __str__(self):
        return self.name


class TestFields(models.Model):
    productivi = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)


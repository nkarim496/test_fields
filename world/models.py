from django.contrib.gis.db import models


class TestFields(models.Model):
    productivi = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)
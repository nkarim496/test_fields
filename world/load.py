import os
from django.contrib.gis.utils import LayerMapping
from .models import WorldBorder, TestFields


world_mapping = {
    'fips' : 'FIPS',
    'iso2': 'ISO2',
    'iso3': 'ISO3',
    'un': 'UN',
    'name': 'NAME',
    'area': 'AREA',
    'pop2005': 'POP2005',
    'region': 'REGION',
    'subregion': 'SUBREGION',
    'lon': 'LON',
    'lat': 'LAT',
    'mpoly': 'MULTIPOLYGON',
}
testfields_mapping = {
    'productivi': 'productivi',
    'geom': 'MULTIPOLYGON',
}

world_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'TM_WORLD_BORDERS-0.3.shp'))
fields_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'test_fields.shp'))


def save_to_db(shp_path, verbose=True):
    lm = LayerMapping(TestFields, shp_path,
                      testfields_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

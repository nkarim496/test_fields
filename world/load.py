import os
from django.contrib.gis.utils import LayerMapping
from .models import WorldBorder, TestFields


testfields_mapping = {
    'productivi': 'productivi',
    'geom': 'MULTIPOLYGON',
}

fields_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'test_fields.shp'))


def save_to_db(shp_path, verbose=True):
    lm = LayerMapping(TestFields, shp_path,
                      testfields_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

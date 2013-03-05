"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils import simplejson as json

from search.tests import save_a_basic_vehicle

class Detailstest(TestCase):
    def test_get_details(self):
        save_a_basic_vehicle()
        response = self.client.get('/details/1/')
        self.assertEqual(json.loads(response.content),
                         {'body': 'SUV',
                          'make': 'Kia',
                          'flag': False,
                          'details': 'http://www.truecar.com/prices-new/kia/sorento-pricing/2014/58BAB7AA',
                          'year': 2014,
                          'model': 'Sorento',
                          'image': 'http://img.truecar.com/colorid_images/v1/959520/175x90/f3q',
                          'MSRP': 24950.0})

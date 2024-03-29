"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import os

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from django.utils import simplejson as json

from models import Vehicle

def save_a_basic_vehicle():
    vehicle = Vehicle(make='Kia',
                      model='Sorento',
                      body='SUV',
                      flag=0,
                      year=2014,
                      MSRP=24950.0,
                      details='http://www.truecar.com/prices-new/kia/sorento-pricing/2014/58BAB7AA',
                      image='http://img.truecar.com/colorid_images/v1/959520/175x90/f3q')
    vehicle.save()
    

class SearchTest(TestCase):
    def test_search(self):
        save_a_basic_vehicle()
        response = self.client.get(reverse('search'), {'term': '2014 kia'})
        self.assertEqual(json.loads(response.content),
                         [{"value": 1, "label": "2014 Kia Sorento SUV"}])

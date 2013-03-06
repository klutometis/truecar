from django.http import HttpResponse
from django.utils import simplejson as json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

from search.models import Vehicle

# http://stackoverflow.com/questions/757022/how-do-you-serialize-a-model-instance-in-django
def details(request, vehicle_id):
    vehicle = Vehicle.objects.get(pk=vehicle_id)
    return HttpResponse(json.dumps({'make': vehicle.make,
                                    'model': vehicle.model,
                                    'body': vehicle.body,
                                    'flag': vehicle.flag,
                                    'year': vehicle.year,
                                    'MSRP': '$' + format(vehicle.MSRP, ',.2f'),
                                    'details': vehicle.details,
                                    'image': vehicle.image}),
                        content_type='application/json')

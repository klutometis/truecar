from django.http import HttpResponse
from django.utils import simplejson as json
from django.core import serializers

from search.models import Vehicle

# http://stackoverflow.com/questions/757022/how-do-you-serialize-a-model-instance-in-django
def details(request, vehicle_id):
    vehicle = Vehicle.objects.get(pk=vehicle_id)
    return HttpResponse(json.dumps(serializers.serialize('json', [ vehicle, ])),
                        content_type='application/json')

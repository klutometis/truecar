from django.http import HttpResponse
from django.utils import simplejson as json

from search.models import Vehicle

# Create your views here.
def search(request):
    (year, make, model, body) = \
        (request.GET.get('term', '').split() + [''] * 4)[:4]
    vehicles = Vehicle.objects\
        .filter(year__startswith=year)\
        .filter(make__istartswith=make)\
        .filter(model__istartswith=model)\
        .filter(body__istartswith=body)\
        .all()\
        .order_by('-year', 'make', 'model', 'body')
    return HttpResponse(json.dumps(list({'label': str(vehicle),
                                         'value': vehicle.id}
                                        for vehicle in vehicles)),
                        content_type='application/json')

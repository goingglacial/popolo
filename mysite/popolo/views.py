from django.core import serializers
from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render_to_response
from django.template import loader, RequestContext
from popolo.models import Popul
import json

def home(request):
    city_dicts = Popul.objects.values('city').distinct()
    cities_list = [str(city_dict['city']) for city_dict in city_dicts]
    all_entries = cities_list
    template = loader.get_template('home.html')
    context = RequestContext(request, {
        'all_entries': all_entries}) 
    return HttpResponse(template.render(context))

def search(request, prefix):
    prefix=prefix.title()
    # cities_data is a LIST of DICTS serialized as JSON
    cities_data = serializers.serialize('json', Popul.objects.all(), fields=('city', 'state', 'pop'))
    # deserialize JSON
    cities_list = json.loads(cities_data)
    # initialize empty list to be populated with dicts for city (by prefix), state, pop
    user_cities = []
    # for dict in cities_list
    for item in cities_list:
        possible_city = item['fields']['city']
        if possible_city.startswith(prefix):
            user_cities.append(item['fields'])
    return HttpResponse (json.dumps(user_cities))
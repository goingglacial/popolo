from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render_to_response
from django.template import loader, RequestContext
from popolo.models import Popul
# import json

def index(request):
    return HttpResponse("Hello, world. Welcome to popolo.")

def home(request):
    city_dicts = Popul.objects.values('city').distinct()
    cities_list = [str(city_dict['city']) for city_dict in city_dicts]
    all_entries = cities_list
    template = loader.get_template('home.html')
    context = RequestContext(request, {
        'all_entries': all_entries}) 
    return HttpResponse(template.render(context))

def bubbles(request):
    template = loader.get_template('bubbles.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def results(request):
    all_entries = Popul.objects.all()
    template = loader.get_template('pops.html')
    context = RequestContext(request, {
        'all_entries': all_entries})
    return HttpResponse(template.render(context))

def random(request):
    all_entries = Popul.objects.all().order_by('?')[:500]
    template = loader.get_template('pops_random.html')
    context = RequestContext(request, {
        'all_entries': all_entries})
    return HttpResponse(template.render(context))

def fifty(request):
    all_entries = Popul.objects.all()[:50]
    template = loader.get_template('50pops.html')
    context = RequestContext(request, {
        'all_entries': all_entries})
    return HttpResponse(template.render(context))

def texas(request):
    all_entries = Popul.objects.filter(state='TX')
    template = loader.get_template('txpops.html')
    context = RequestContext(request, {
        'all_entries': all_entries})
    return HttpResponse(template.render(context))

def about(request):
    return HttpResponse("This is the about page.")

names_dict =    {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

def states(request, statename):
    state_dicts = Popul.objects.values('state').distinct()
    states_list = [state_dict['state'] for state_dict in state_dicts]
    # return HttpResponse(json.dumps(states_list))
    statename = statename.upper()
    if statename in states_list:
        all_entries = Popul.objects.filter(state=statename)
        template = loader.get_template('anyState.html')
        context = RequestContext(request, {
            'all_entries': all_entries, 'statename': names_dict[statename]})
        return HttpResponse(template.render(context))
    else:
        template = loader.get_template('error.html')
        context = RequestContext(request, {
            'statename': statename})
        return HttpResponse(template.render(context))

def search(request, prefix):
    print prefix
    all_entries = Popul.objects.filter(city__startswith=prefix)
    template = loader.get_template('testpops.html')
    context = RequestContext(request, {
        'all_entries': all_entries})
    return HttpResponse(template.render(context))
    # print all_entries
    # return StreamingHttpResponse(all_entries)
    
    '''
    take prefix user has typed, query database, get results, convert to json, convert
    to over-the-wire json to 
    '''
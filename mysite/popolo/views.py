from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader, RequestContext
from popolo.models import Popul

def index(request):
    return HttpResponse("Hello, world. Welcome to popolo.")

def home(request):
    template = loader.get_template('home.html')
    context = RequestContext(request)
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

names_dict =    {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
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
        'MP': 'Northern Mariana Islands',
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
        'PR': 'Puerto Rico',
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
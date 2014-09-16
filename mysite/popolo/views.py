from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader, RequestContext
from popolo.models import Popul

def index(request):
    return HttpResponse("Hello, world. Welcome to popolo.")

def results(request):
    all_entries = Popul.objects.all()
    template = loader.get_template('pops.html')
    context = RequestContext(request, {
        'all_entries': all_entries})
    return HttpResponse(template.render(context))

def random(request):
    all_entries = Popul.objects.all().order_by('?')[:500]
    template = loader.get_template('pops.html')
    context = RequestContext(request, {
        'all_entries': all_entries})
    return HttpResponse(template.render(context))
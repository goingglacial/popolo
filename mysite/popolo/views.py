from django.http import HttpResponse
from django.shortcuts import render_to_response
from popolo.models import Popul

def index(request):
    return HttpResponse("Hello, world. Welcome to popolo.")

def results(request):
    query_results = Popul.objects.all()
    #return a response to your template and add query_results to the context
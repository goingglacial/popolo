from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. Welcome to popolo.")

def results(request):
    return HttpResponse("Here's some U.S. population data.")
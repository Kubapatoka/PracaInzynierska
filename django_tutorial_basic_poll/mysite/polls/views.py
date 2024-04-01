from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World, it is a simple poll app. Index")
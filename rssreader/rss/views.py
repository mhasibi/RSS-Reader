from django.http import HttpResponse

def index(request):
    return HttpResponse("RSS Reader Index View")

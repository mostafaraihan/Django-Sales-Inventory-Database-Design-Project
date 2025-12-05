from django.http import HttpResponse

def index(request):
    return HttpResponse("Django Sales and Inventory Database Design")
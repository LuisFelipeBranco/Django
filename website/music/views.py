from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Music app created!!</h1>")

def detail(request, album_id):
    return HttpResponse("<h2>Details for Album ID: " + str(album_id) + "</h2>")
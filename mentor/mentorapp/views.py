from django.http import HttpResponse

def index(request):
    return HttpResponse("Mehul Sharma & Achint Sharma says hey there world!")

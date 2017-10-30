from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage' : "I am a bold message"}
    return render(request,'mentorapp/index.html',context_dict)


def about(request) :
    return HttpResponse("This is the about page <br/> <a href='/mentor/'>Home</a>")

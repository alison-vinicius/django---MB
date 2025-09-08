from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloWorld(request):
    return HttpResponse("olá mundo")
def taskList(request):
    return render(request, 'tasks/list.html')

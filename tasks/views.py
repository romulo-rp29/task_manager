from django.shortcuts import render
from tasks.models import Task

# Create your views here.


def index(request):
    context = {"tasks": Task.objects.all()}
    return render(request, "home.html", context)

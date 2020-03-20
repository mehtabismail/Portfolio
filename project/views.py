from django.shortcuts import render
from .models import project
# Create your views here.
def home(request):
    variable = project.objects
    return render(request, 'project/index.html', {'projects': variable})


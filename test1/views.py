from django.shortcuts import render
from about.models import about
def index(request):
    variable = about.objects
    return render(request, 'index.html', {'var_about': variable})


def home(request):
    return render(request, 'home.html')



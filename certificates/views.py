from django.shortcuts import render
from .models import certificate
# Create your views here.
def home(request):
    variable = certificate.objects
    return render(request, 'certificates/index.html', {'certificates': variable})
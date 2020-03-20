from django.shortcuts import render
from . models import blog


# Create your views here.
def home(request):
    blog_variable = blog.objects
    return render(request, 'blog/index.html', {'blogs': blog_variable})


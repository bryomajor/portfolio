from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import Project

# Create your views here.
def index(request):
    return render(request, 'index.html')
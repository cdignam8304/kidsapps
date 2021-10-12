# from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import ListView
from animals.models import Animal

# Create your views here.

# def index(request):
# 	return HttpResponse("Hello, world. You're at the animals index.")

class AnimalListView(ListView):
    model = Animal



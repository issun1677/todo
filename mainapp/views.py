from django.shortcuts import render
from .models import Todotext
# Create your views here.

def home(request):

	todo = Todotext.objects.all()

	return render(request, "mainapp/index.html")

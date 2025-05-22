from django.shortcuts import render
from .models import Course

def index(request):
    courses = Course.objects.all()
    return render(request, 'courses/index.html', {'courses': courses})

def details(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'courses/details.html', {'course': course})
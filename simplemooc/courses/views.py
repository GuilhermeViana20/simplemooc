from django.shortcuts import render, get_object_or_404
from .models import Course

def index(request):
    courses = Course.objects.all()
    return render(request, 'courses/index.html', {'courses': courses})

# def details(request, pk):
#     course = get_object_or_404(Course, pk=pk)
#     return render(request, 'courses/details.html', {'course': course})

def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    return render(request, 'courses/details.html', {'course': course})
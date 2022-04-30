from django.shortcuts import render
from .models import Courses, About
# Create your views here.
def about(request):
    courses = Courses.objects.all()
    contents = About.objects.all()
    return render(request, 'courses/about.html', {'courses':courses[0:3], 'contents':contents})

def courses(request):
    courses = Courses.objects.all()
    return render(request, 'courses/courses.html', {'courses':courses})
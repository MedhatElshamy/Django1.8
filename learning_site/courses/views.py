from django.shortcuts import render
from .models import Course
from django.http import HttpResponse
# Create your views here.

# def courses_list(request):
# 	courses = Course.objects.all()
# 	output = ', '.join([str(course) for course in courses])
	
# 	return HttpResponse(output)

def course_list(request):
	courses = Course.objects.all()
	return render(request, 'courses/course_list.html', {'courses': courses})
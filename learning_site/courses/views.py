from django.shortcuts import get_object_or_404, render
from .models import Course, Step
from django.http import HttpResponse
# Create your views here.

# def courses_list(request):
# 	courses = Course.objects.all()
# 	output = ', '.join([str(course) for course in courses])
	
# 	return HttpResponse(output)

def course_list(request):
	courses = Course.objects.all()
	email = 'questions@learning-site.com'
	context = {'courses': courses, 'email': email}
	return render(request, 'courses/course_list.html', context)

def course_detail(request, pk):
	# course = Course.objects.get(pk = pk)
	course = get_object_or_404(Course, pk=pk)
	return render(request, 'courses/course_detail.html', {'course': course})

def step_detail(request, course_pk, step_pk):
	step = get_object_or_404(Step, course_id=course_pk, pk=step_pk)
	return render(request, 'courses/step_detail.html', {'step':step})
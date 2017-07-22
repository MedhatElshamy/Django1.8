from django import template
from courses.models import Course
import markdown2
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def newest_course():
	''' Get Our Latest Course '''
	return Course.objects.latest('created_at')

@register.inclusion_tag('courses/course_nav.html')
def nav_courses_list():
	''' Return dictionary of courses to display as navigation pane. '''
	courses = Course.objects.all()
	return {'courses': courses}

@register.filter('time_estimate')
def time_estimate(word_count):
	''' Estimate The Number Of Minutes It Will Take To Complete A Step Based On The Passed-In Wordcount. '''
	minutes = round(word_count/20)
	return minutes

@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
	html_body = markdown2.markdown(markdown_text)
	return mark_safe(html_body)
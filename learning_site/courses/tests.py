from django.test import TestCase
from .models import Course,Step
from django.utils import timezone
# Create your tests here.


class CourseModelTests(TestCase):
	def test_course_creation(self):
		course = Course.objects.create(
			title='Reqular Expressions',
			description='Learn To Write RegEx In Python'
		)
		now = timezone.now()
		self.assertLess(course.created_at, now)

# class StepModelTests(TestCase):
# 	def test_step_creation(self):
# 		step = Step.objects.create(
# 			title="Python's syntax",
# 			description='Learn about Python',
# 			course=self.course
# 		)

# 		self.assertIn(step, self.objects.step_set.all())

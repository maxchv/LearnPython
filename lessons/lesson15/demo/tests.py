from django.test import TestCase
from .models import Teacher
from django.contrib.auth.models import User


class SimpleTest(TestCase):
    def setUp(self):
        user = User.objects.create(username="user", password="password")
        Teacher.objects.create(user=user, phone="test")

    def contains_teachers(self):
        self.assertEqual(1, Teacher.objects.count())
from django.test import TestCase
from demo.models import User


# Create your tests here.
class FooTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        User.objects.create(username="user", password="qwerty")

    def test(self):
        self.assertEqual(2, 2)

    def testIfUserExists(self):
        self.assertEqual(User.objects.count(), 2)

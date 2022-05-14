from unittest import TestCase

from demo.models import Task


class TaskTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # print("setUpClass()")

    def setUp(self):
        # print("setUp()")
        Task.objects.all().delete()
        Task.objects.create(description="My first task")

    def tearDown(self):
        Task.objects.all().delete()

    def test_task_exists(self):
        self.assertEqual(1, Task.objects.count())

    def test_task_should_have_proper_description(self):
        task = Task.objects.first()
        self.assertEqual("My first task", task.description)
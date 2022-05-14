from django.test import TestCase, Client
from django.urls import reverse

from demo.models import Task


class TestAddTask(TestCase):

    def setUp(self):
        self.c = Client()
        Task.objects.all().delete()

    def tests_not_found(self):
        r = self.c.get('/kjalkjfakljfs')
        self.assertEqual(404, r.status_code)

    def tests_check_empty_view(self):
        response = self.c.get(reverse('demo:index'))
        self.assertEqual(200, response.status_code)
        self.assertEqual('demo/index.html', response.template_name[0])
        self.assertEqual('Demo', response.context[0]['title'])
        self.assertTrue(response.context[0].get('form') is not None)
        self.assertTrue(response.context[0].get('tasks') is not None)
        self.assertEqual(response.context[0].get('tasks').count(), 0)
        self.assertContains(response, '<p>Empty task lists</p>', 1)
        html = response.content.decode('utf-8')
        self.assertInHTML('<p>Empty task lists</p>', html, 1)

    def tests_create_task(self):
        self.assertEqual(Task.objects.count(), 0)
        response = self.c.post(reverse('demo:index'),
                               {'description': 'Test task'})
        # self.assertEqual(reverse('demo:index'), response.redirect_chain[0])
        self.assertEqual(reverse('demo:index'), response.headers['Location'])
        self.assertEqual(302, response.status_code)
        self.assertEqual(Task.objects.count(), 1)
        task = Task.objects.first()
        self.assertEqual(task.description, 'Test task')

    def tests_create_task_and_check_list(self):
        self.assertEqual(Task.objects.count(), 0)
        response = self.c.post(reverse('demo:index'),
                               {'description': 'Test task'}, follow=True)
        self.assertEqual(200, response.status_code)
        self.assertEqual(Task.objects.count(), 1)
        self.assertContains(response, '<div class="tasks">', 1)
        self.assertContains(response, '<div class="task">', 1)

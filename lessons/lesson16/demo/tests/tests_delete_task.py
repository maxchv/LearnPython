from django.test import TestCase, Client
from django.urls import reverse

import demo.views
from demo.models import Task


class DeleteTaskTestCase(TestCase):

    def setUp(self):
        self.c = Client()
        Task.objects.all().delete()
        self.task = Task.objects.create(description='First task')

    def test_delete_task_get_request(self):
        """
        При отправить GET запроса по пути /delete/<int:pk> отображается темплейт,
        в котором есть элемент <p>Are you sure you want to delete task "{{ object }}"?</p>
        """
        url = reverse('demo:delete', args=(self.task.pk,))
        r = self.c.get(url)
        expected_status_code = 200
        self.assertEqual(expected_status_code, r.status_code)
        self.assertEqual('demo/task_confirm_delete.html', r.template_name[0])
        self.assertContains(r, f'<p>Are you sure you want to delete task "{self.task}"?</p>', 1)
        self.assertContains(r, '<form method="post">', 1)
        self.assertTrue(Task.objects.contains(self.task))
        self.assertTrue(r.resolver_match.func.__name__, demo.views.TasksDeleteView.as_view().__name__)

    def test_delete_task_post_request(self):
        """
        При отправить POST запроса по пути /delete/<int:pk>
            производится перенаправление по пути /
            удаляется таска из базы данных
        """
        url = reverse('demo:delete', args=(self.task.pk,))
        r = self.c.post(url, follow=True)
        redirect_url = reverse('demo:index')
        status_code = 302
        self.assertEqual(r.redirect_chain[0], (redirect_url, status_code))
        self.assertFalse(Task.objects.contains(self.task))
        self.assertContains(r, '<p>Empty task lists</p>', 1)
        self.assertNotContains(r, '<div class="tasks">')
        self.assertNotContains(r, '<div class="task">')
        self.assertTrue(r.resolver_match.func.__name__, demo.views.TasksDeleteView.as_view().__name__)

from django.urls import reverse
from rest_framework.test import APITestCase

from demo.models import Post, Comment


class PostTestCase(APITestCase):

    def test_create_post(self):
        count = Post.objects.count()
        end_point = reverse('demo:posts-list')
        self.client.post(end_point, {'title': 'Test post'}, format='json')
        self.assertEqual(Post.objects.count(), count + 1)
        post = Post.objects.last()
        self.assertEqual(post.title, 'Test post')
        response = self.client.get(end_point, format='json')
        for d in response.data['results']:
            d.pop('created')
        self.assertEqual(response.data['results'], [{'id': 1, 'title': 'Test post', 'text': None, 'comments': []}])


class CommentTestCase(APITestCase):

    def test_create_comment(self):
        p = Post.objects.create(title='First post')
        count = Comment.objects.count()
        end_point = reverse('demo:comments-list')
        self.client.post(end_point, {'text': 'Comment', 'post': p.id}, format='json')
        self.assertEqual(Comment.objects.count(), count + 1)
        response = self.client.get(end_point, format='json')
        for d in response.data['results']:
            d.pop('created')
        self.assertEqual(response.data['results'], [{'id': 1, 'text': 'Comment', 'post': p.id}])

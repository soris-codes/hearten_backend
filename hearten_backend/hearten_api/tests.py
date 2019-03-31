from .models import Post
from .serializers import PostSerializer
from django.urls import reverse

from knox.models import AuthToken
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
import json

class PostListCreateAPIViewTestCase(APITestCase):
    # url = 'api/posts/'
    url = reverse('posts-list')

    # Set up user and token
    def setUp(self):
        self.username = "joe"
        self.email = "joe@me.com"
        self.password = "12345678"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = AuthToken.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token[1])

    def test_create_post(self):
        response = self.client.post(self.url, {
          "title": "Test post",
          "body": "This is my test post",
          })
        self.assertEqual(201, response.status_code)

    def test_user_posts(self):
        """
        Test to verify user posts list
        """
        Post.objects.create(author=self.user, title="Test post", body="Another post")
        response = self.client.get(self.url)
        self.assertTrue(len(json.loads(response.content)) == Post.objects.count())



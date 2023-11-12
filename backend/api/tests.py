from django.test import TestCase
from .models import Blog
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from . import views
# Create your tests here.




"""Test models."""
class ModelTestApi(TestCase): 


    def test_create_blog(self):
        """Teste create a new blog instance."""

        body = "cachorro"
        new = Blog.objects.create(
            body = body,
        )
        new.save()

        """Test body igual a new.body."""
        self.assertEqual(new.body, body)


"""Test views."""
class ViewTestApi(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
    

    def test_create_blog_view_201_CREATED(self):
        """Test a create new blog view. If returns 201 HTTP status, its ok."""
        
        data = {'body': 'create new blog.'}
        request = self.client.post(
            reverse('create'),
            data,
        )

        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Blog.objects.count(), 1)
        new_blog = Blog.objects.get()
        print(new_blog)
        self.assertEqual(new_blog.body, 'create new blog.')
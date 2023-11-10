from django.test import TestCase
from .models import Blog
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

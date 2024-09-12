from django.test import TestCase
from .models import Blog,Author

class AuthorTest(TestCase):
    
    def setUp(self):
        Blog.objects.create(name="Tech Blog",tagline="All About Tech Blog")
        # Blog.objects.create(name='Medical Blog',tagline="All about Medical Blog")
    
    def test_blog_creation(self):
        blog = Blog.objects.get(name="Tech Blog")
        self.assertEqual(blog.tagline,"All About Tech Blog")
    
    def test_auth_str_creation(self):
        blog = Blog.objects.get(name='Tech Blog')
        self.assertEqual(str(blog),'Tech Blog')
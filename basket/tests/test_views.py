from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from store.models import Category, Product

class TestBasketView(TestCase):
    def setUp(self):
        User.objects.create(user='admin')
        Category.objects.create(name='django', slug='django')
        Product.objects.create(category_id=1, title='django beginners', created_by_id=1, slug)
from django.test import TestCase

from .models import Category
from .models import Article

class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(category='Innovations', slug='Innovations')

    def test_get_absolute_url(self):
        category = Category.objects.get(id=1)

        self.assertEquals(category.get_absolute_url(), '/articles/category/Innovations')


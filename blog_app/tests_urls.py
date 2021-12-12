from django.test import TestCase
from django.urls import reverse, resolve
from .views import HomePageView
from .models import Article, Category

class HomeTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(category='Innovations', slug='innovations')
        cls.article = Article.objects.create(title = 'newtitle', category = cls.category, slug='newtitle')

    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, HomePageView)

    def test_category_view_status_code(self):
        url = reverse('articles-category-list', args=('name',))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_list_view_status_code(self):
        url = reverse('articles-list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_detail_view_status_code(self):
        url = reverse('news-detail', kwargs={'year': self.article.pub_date.strftime("%Y"),
                                       'month': self.article.pub_date.strftime("%m"),
                                       'day': self.article.pub_date.strftime("%d"),
                                       'slug': self.article.slug,   })
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)



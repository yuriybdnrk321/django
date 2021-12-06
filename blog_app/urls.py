from django.urls import path
from blog_app import views

urlpatterns = [
    path(r'', views.HomePageView.as_view()),
]
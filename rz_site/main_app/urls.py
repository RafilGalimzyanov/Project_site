from django.urls import path
from main_app import views


urlpatterns = [
    path('', views.index, name='index'),
    path('work_examples', views.work_examples, name='work_examples'),
    path('reviews', views.reviews, name='reviews'),
    path('articles', views.articles, name='articles'),
    path('authorization', views.authorization, name='authorization'),
]
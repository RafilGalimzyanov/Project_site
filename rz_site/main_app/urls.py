from django.urls import path
from main_app.views import index, work_examples, reviews, articles, RegisterUser, out_from_account, authorization


urlpatterns = [
    path('', index, name='index'),
    path('work_examples/', work_examples, name='work_examples'),
    path('reviews/', reviews, name='reviews'),
    path('articles/', articles, name='articles'),
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('logout/', out_from_account, name='logout'),
    path('authorization/', authorization, name='authorization'),
]
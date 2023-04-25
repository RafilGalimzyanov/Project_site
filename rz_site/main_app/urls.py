from django.urls import path
from main_app.views import index, work_examples, reviews, articles, authorization, registration, account, logout


urlpatterns = [
    path('', index, name='index'),
    path('work_examples/', work_examples, name='work_examples'),
    path('reviews/', reviews, name='reviews'),
    path('articles/', articles, name='articles'),
    path('authorization/', authorization, name='authorization'),
    path('registration/', registration, name='registration'),
    path('account/', account, name='account'),
    path('logout/', logout, name='logout'),
]
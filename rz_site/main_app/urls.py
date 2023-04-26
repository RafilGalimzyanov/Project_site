from django.urls import path
from main_app.views import index, work_examples, reviews, articles, account, logout_for_user, \
    RegisterUser, LoginUser, AddReview

urlpatterns = [
    path('', index, name='index'),
    path('work_examples/', work_examples, name='work_examples'),
    path('reviews/', reviews, name='reviews'),
    path('articles/', articles, name='articles'),
    path('authorization/', LoginUser.as_view(), name='authorization'),
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('account/', account, name='account'),
    path('logout/', logout_for_user, name='logout'),
    path('add_review/', AddReview.as_view(), name='add_review'),

]
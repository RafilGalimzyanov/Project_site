from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from .forms import RegisterUserForm, LoginUserForm, AddReviewForm
from .models import Review, Articles
from .utils import disciplines_list, advantages_list


def index(request):
    all_articles = Articles.objects.all()
    context = {'disciplines_list': disciplines_list, 'recent_reviews': all_articles, 'advantages_list': advantages_list}
    return render(request, 'main_app/index.html', context=context)


def work_examples(request):
    return render(request, 'main_app/work_examples.html')


def reviews(request):
    all_reviews = Review.objects.all()
    context = {
        'reviews': all_reviews,
    }
    return render(request, 'main_app/reviews.html', context=context)


def articles(request):
    all_articles = Articles.objects.all()
    context = {
        'articles': all_articles,
    }
    return render(request, 'main_app/articles.html', context=context)


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main_app/authorization.html'

    def get_success_url(self):
        return reverse_lazy('index')
    

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main_app/registration.html'
    success_url = reverse_lazy('reviews')

    def form_valid(self, form_class):
        user = form_class.save()
        login(self.request, user)
        return redirect('index')


def account(request):
    return render(request, 'main_app/account.html')


def logout_for_user(request):
    logout(request)
    return render(request, 'main_app/index.html')


class AddReview(FormView):
    form_class = AddReviewForm
    template_name = 'main_app/add_review.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')
        return render(request, self.template_name, {'form': form})

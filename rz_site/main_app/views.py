from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm, LoginUserForm
from .models import Review


def index(request):
    if request.user.is_authenticated:
        return render(request, 'main_app/index.html')
    return render(request, 'main_app/index.html')


def work_examples(request):
    return render(request, 'main_app/work_examples.html')


def reviews(request):
    all_reviews = Review.objects.all()
    context = {
        'reviews': all_reviews,
    }
    return render(request, 'main_app/reviews.html', context=context)


def articles(request):
    return render(request, 'main_app/articles.html')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main_app/authorization.html'
    success_url = reverse_lazy('index')
    

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main_app/registration.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form_class):
        user = form_class.save()
        login(self.request, user)
        return redirect('index')


def account(request):
    return render(request, 'main_app/account.html')


def logout(request):
    return render(request, 'main_app/index.html')
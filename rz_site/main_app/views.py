from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm
from .models import Review


def index(request):
    if request.user.is_authenticated:
        return render(request, 'main_app/index.html', context={'user_info': 'Авторизован', 'menu': menu, })
    return render(request, 'main_app/index.html', context={'menu': menu, })


def work_examples(request):
    return render(request, 'main_app/work_examples.html', context={'menu': menu, })


def reviews(request):
    all_reviews = Review.objects.all()
    context = {
        'reviews': all_reviews,
        'menu': menu,
    }
    return render(request, 'main_app/reviews.html', context=context)


def articles(request):
    return render(request, 'main_app/articles.html', context={'menu': menu, })


def registration(request):
    return render(request, 'main_app/registration.html', context={'menu': menu, })


def out_from_account(request):
    logout(request)
    return redirect('index')


def authorization(request):
    return render(request, 'main_app/authorization.html')
    
    
def registration(request):
    return render(request, 'main_app/registration.html')


def account(request):
    return render(request, 'main_app/account.html')


def logout(request):
    return render(request, 'main_app/index.html')
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm
from .models import Review


def index(request):
    if request.user.is_authenticated:
        return render(request, 'main_app/index.html', context={'user_info': 'Авторизован'})
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


def authorization(request):
    return render(request, 'main_app/authorization.html')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main_app/authorization.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(context.items())

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')
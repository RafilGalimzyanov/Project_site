from django.shortcuts import render
from .models import Review


def index(request):
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

from django.shortcuts import render


def index(request):
    return render(request, 'main_app/index.html')


def work_examples(request):
    return render(request, 'main_app/work_examples.html')


def reviews(request):
    return render(request, 'main_app/reviews.html')


def articles(request):
    return render(request, 'main_app/articles.html')


def authorization(request):
    return render(request, 'main_app/authorization.html')

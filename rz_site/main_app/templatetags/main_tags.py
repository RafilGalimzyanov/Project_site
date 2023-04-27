from django import template
from main_app.models import *


register = template.Library()


@register.inclusion_tag('main_app/recent_reviews.html')
def show_reviews():
    reviews = Review.objects.all()
    if len(reviews) >= 3:
        reviews = reviews.order_by('-pk')[:3]
    return {"reviews": reviews}
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from lachesis.models import Category
from lachesis.models import Page

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'boldmessage' : "This app was developed with the authors as well as the readers in mind."}
    return render(request, 'lachesis/index.html', context=context_dict)
def about(request):
    return HttpResponse("This is the about page. <a href='/lachesis/'>View index page</a>")

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'lachesis/category.html', context_dict)

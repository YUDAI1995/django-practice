from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class index_page(TemplateView):
    template_name = 'app/index.html'

def title(request):
    return HttpResponse('<h1>Hello, World!</h1>')

def user_page(request, user_name):
    return HttpResponse(f'<h1>{user_name}\'s page</h1>')

def number_page(request, number):
    return HttpResponse(f'<h1>article number {number}</h1>')
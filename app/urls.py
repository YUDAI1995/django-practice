from django.urls import path
from . import views


app_name = 'app'

urlpatterns = [
    path('', views.index_page.as_view(), name='index'),
    path('first/', views.title, name='title'),
    path('user/<str:user_name>', views.user_page, name='user_page'),
    path('article/<int:number>', views.number_page, name='number_page')
]
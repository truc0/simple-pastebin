from django.urls import path

from .views import index, create, detail

app_name = 'snippets'
urlpatterns = [
    path('', index, name='index'),
    path('create', create, name='create'),
    path('<int:pk>', detail, name='detail'),
]
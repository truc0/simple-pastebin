from django.urls import path

from .views import index, detail

app_name = 'snippets'
urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>', detail, name='detail'),
]
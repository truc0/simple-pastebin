from django.urls import path

from .views import IndexView, create, detail

app_name = 'snippets'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create', create, name='create'),
    path('<int:pk>', detail, name='detail'),
]
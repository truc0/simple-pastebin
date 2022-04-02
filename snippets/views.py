from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Snippet

# Create your views here.
def index(request):
    pianduan = Snippet.objects.all()
    return render(request, 'index.html', context={ 'snippets': pianduan })


def detail(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    return render(request, 'detail.html', context={ 'snippet': snippet })

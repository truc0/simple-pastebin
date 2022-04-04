from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import Snippet
from .forms import SnippetForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        language = request.POST['language']
        code = request.POST.get('code')
        form = SnippetForm(request.POST)
        # if language == '':
        #     return HttpResponse('Language cannot be empty')
        # if code == '':
        #     return HttpResponse('Code cannot be empty')
        if form.is_valid():
            snippet = Snippet.objects.create(language=language, code=code)
            return redirect('snippets:detail', pk=snippet.id)
        else:
            return HttpResponse('Code cannot be empty and language cannot be empty')
    else:
        snippets = Snippet.objects.all()
        return render(request, 'index.html', context={ 'snippets': snippets })


def detail(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    return render(request, 'detail.html', context={ 'snippet': snippet })


def create(request):
    return render(request, 'create.html', context={ 'form': SnippetForm() })
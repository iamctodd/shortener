from django.shortcuts import get_object_or_404, redirect, render

from .models import URL
from . import forms 

# Create your views here.
def root(request, url_hash):
    url = get_object_or_404(URL, url_hash=url_hash)
    url.clicked()

    return redirect(url.full_url)

def link_view(request):
	form = forms.LinktoShorten()
	return render (request, 'link.html', {'form': form})

def index(request):
    return render(request, 'index.html', {})
    
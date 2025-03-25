from django.shortcuts import render, get_object_or_404
from .models import Page
from .forms import PageForm

def page_list(request):
    pages = Page.objects.all()  # Obtém todas as páginas do banco de dados
    return render(request, 'pages/page_list.html', {'pages': pages})

def page_detail(request, pk):
    page = get_object_or_404(Page, pk=pk)  # Busca a página específica pelo ID
    return render(request, 'pages/page_detail.html', {'page': page})

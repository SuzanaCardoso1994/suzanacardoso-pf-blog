from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Page
from .forms import PageForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

# Exibir a lista de páginas
def page_list(request):
    pages = Page.objects.all()
    return render(request, 'pages/page_list.html', {'pages': pages})

# Detalhes de uma página
def page_detail(request, pk):
    page = get_object_or_404(Page, pk=pk)
    return render(request, 'pages/page_detail.html', {'page': page})

def logout_view(request):
    logout(request)
    return redirect('home')

# Criar uma nova página
@login_required
def page_create(request):
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('page_list')  # Redireciona para a lista de páginas
    else:
        form = PageForm()
    return render(request, 'pages/page_form.html', {'form': form})

# Editar uma página existente
@login_required
def page_edit(request, pk):
    page = get_object_or_404(Page, pk=pk)
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES, instance=page)
        if form.is_valid():
            form.save()
            return redirect('page_detail', pk=page.pk)  # Redireciona para a página de detalhes
    else:
        form = PageForm(instance=page)
    return render(request, 'pages/page_form.html', {'form': form})

# Excluir uma página
@login_required
def page_delete(request, pk):
    page = get_object_or_404(Page, pk=pk)
    page.delete()
    return redirect('page_list')  # Redireciona para a lista de páginas

@login_required
def profile(request):
    return render(request, 'profile.html')

# Editar perfil do usuário
@login_required
def edit_profile(request):
    if request.method == 'POST':
        # Lógica de edição de perfil
        pass
    return render(request, 'edit_profile.html')
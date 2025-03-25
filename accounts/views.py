from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

# View para exibir o formulário de registro
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Loga o usuário automaticamente após o registro
            messages.success(request, 'Registro realizado com sucesso!')
            return redirect('home')  # Redireciona para a home após o registro
        else:
            messages.error(request, 'Erro no registro. Tente novamente.')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

# View para exibir o formulário de login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Você foi logado com sucesso!')
            return redirect('home')  # Redireciona para a home após o login
        else:
            messages.error(request, 'Credenciais inválidas. Tente novamente.')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# View para deslogar o usuário
def user_logout(request):
    logout(request)
    messages.success(request, 'Você foi deslogado com sucesso!')
    return redirect('home')  # Redireciona para a home após o logout
def about(request):
    # Aqui você pode colocar qualquer informação que queira mostrar sobre o proprietário da página
    owner_info = {
        'name': 'Suzana Cardoso',
        'bio': 'Sou desenvolvedora e criadora de conteúdo, apaixonada por programação e design.',
        'contact': 'suzanaoliv1994@gmail.com',
        'image': 'path_to_owner_image.jpg',  # Se você tiver uma imagem do proprietário, pode usar essa chave
    }
    return render(request, 'about.html', {'owner_info': owner_info})

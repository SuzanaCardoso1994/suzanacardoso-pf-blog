from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),  # Rota de login
    path('logout/', views.user_logout, name='logout'),  # Rota de logout
    path('register/', views.register, name='register'),  # Rota de registro
    path('about/', views.about, name='about'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('pages/', views.page_list, name='page_list'),  # Exibe a lista de páginas
    path('pages/<int:pk>/', views.page_detail, name='page_detail'),  # Exibe os detalhes da página
    path('pages/new/', views.page_create, name='page_create'),  # Criação de uma nova página
    path('pages/<int:pk>/edit/', views.page_edit, name='page_edit'),  # Editar uma página
    path('pages/<int:pk>/delete/', views.page_delete, name='page_delete'),  # Excluir uma página
]

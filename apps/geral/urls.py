from django.urls import path
from . import views

app_name = 'geral'

urlpatterns = [
    path('nova-oficina', views.nova_oficina, name='nova_oficina'),
    path('oficinas/', views.lista_oficina, name='lista_oficina'),
    path('excluir_oficina/<int:pk>/', views.apagar_oficina, name='apagar_oficina'),
    path('editar_oficina/<int:pk>/', views.editar_oficina, name='editar_oficina'),
    path('', views.home, name='home'),
    
]
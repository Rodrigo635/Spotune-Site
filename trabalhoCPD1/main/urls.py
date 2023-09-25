from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('saiba-mais/', views.saiba_mais, name='saibamais'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('sair/', views.sair, name='sair'),
    path('playlist/', views.playlist, name='playlist'),
]
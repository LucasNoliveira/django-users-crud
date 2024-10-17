from django.urls import path
from . import views

urlpatterns = [
    path('licoes/', views.listar_licoes, name='listar_licoes'),
    path('licoes/criar/', views.criar_licao, name='criar_licao'),
    path('licoes/<int:id>/editar-html/', views.editar_html_licao, name='editar_html_licao'),
    path('licoes/<int:id>/deletar/', views.deletar_licao, name='deletar_licao'),
]

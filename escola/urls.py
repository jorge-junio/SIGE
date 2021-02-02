from django.urls import path
from .views import listarEscola
from .views import adicionarEscola
from .views import editarEscola
from .views import excluirEscola

urlpatterns = [
    path('listar/', listarEscola, name='listarEscola'),
    path('adicionar/', adicionarEscola, name='adicionarEscola'),
    path('editar/<int:id>/', editarEscola, name='editarEscola'),
    path('excluir/<int:id>/', excluirEscola, name='excluirEscola'),
]

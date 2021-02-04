from django.urls import path
from .views import listarEscola, adicionarEscola, editarEscola, excluirEscola
from .views import listarTurma, adicionarTurma, editarTurma, excluirTurma
from .views import listarAluno, adicionarAluno, editarAluno, excluirAluno
from .views import listarProfessor, adicionarProfessor, editarProfessor, excluirProfessor
from .views import listarDisciplina, adicionarDisciplina, editarDisciplina, excluirDisciplina
from .views import listarHabilidade, adicionarHabilidade, editarHabilidade, excluirHabilidade

urlpatterns = [
    path('listar/', listarEscola, name='listarEscola'),
    path('adicionar/', adicionarEscola, name='adicionarEscola'),
    path('editar/<int:id>/', editarEscola, name='editarEscola'),
    path('excluir/<int:id>/', excluirEscola, name='excluirEscola'),

    path('listarTurma/', listarTurma, name='listarTurma'),
    path('adicionarTurma/', adicionarTurma, name='adicionarTurma'),
    path('editarTurma/<int:id>/', editarTurma, name='editarTurma'),
    path('excluirTurma/<int:id>/', excluirTurma, name='excluirTurma'),

    path('listarAluno/', listarAluno, name='listarAluno'),
    path('adicionarAluno/', adicionarAluno, name='adicionarAluno'),
    path('editarAluno/<int:id>/', editarAluno, name='editarAluno'),
    path('excluirAluno/<int:id>/', excluirAluno, name='excluirAluno'),

    path('listarProfessor/', listarProfessor, name='listarProfessor'),
    path('adicionarProfessor/', adicionarProfessor, name='adicionarProfessor'),
    path('editarProfessor/<int:id>/', editarProfessor, name='editarProfessor'),
    path('excluirProfessor/<int:id>/', excluirProfessor, name='excluirProfessor'),

    path('listarDisciplina/', listarDisciplina, name='listarDisciplina'),
    path('adicionarDisciplina/', adicionarDisciplina, name='adicionarDisciplina'),
    path('editarDisciplina/<int:id>/', editarDisciplina, name='editarDisciplina'),
    path('excluirDisciplina/<int:id>/', excluirDisciplina, name='excluirDisciplina'),

    path('listarHabilidade/', listarHabilidade, name='listarHabilidade'),
    path('adicionarHabilidade/', adicionarHabilidade, name='adicionarHabilidade'),
    path('editarHabilidade/<int:id>/', editarHabilidade, name='editarHabilidade'),
    path('excluirHabilidade/<int:id>/', excluirHabilidade, name='excluirHabilidade'),
]

from django.forms import ModelForm
from .models import Escola, Turma, Aluno, Professor, Disciplina, Habilidade

class EscolaForm(ModelForm):
    class Meta:
        model = Escola
        fields = ['nome', 'descricao', 'telefone', 'email']


class TurmaForm(ModelForm):
    class Meta:
        model = Turma
        fields = ['nome', 'descricao', 'codigoEscola']

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'sobrenome', 'descricao', 'telefone', 'email']

class ProfessorForm(ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'sobrenome', 'descricao', 'telefone', 'email']

class DisciplinaForm(ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome', 'descricao',]

class HabilidadeForm(ModelForm):
    class Meta:
        model = Habilidade
        fields = ['nome', 'descricao', 'recompensa']
from django.contrib import admin
from .models import Escola, Turma, Aluno, Professor, Disciplina, Habilidade

# Register your models here.
admin.site.register(Escola)
admin.site.register(Turma)
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Disciplina)
admin.site.register(Habilidade)
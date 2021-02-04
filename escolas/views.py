from django.shortcuts import render, redirect, get_object_or_404
from .models import Escola, Turma, Aluno, Professor, Disciplina, Habilidade
from .forms import EscolaForm, TurmaForm, AlunoForm, ProfessorForm, DisciplinaForm, HabilidadeForm

# Create your views here.
#funções da entidade Escola
def listarEscola(request):
    nome = request.GET.get('nome', None)

    escolas = Escola.objects.all()

    return render(request, 'escola/listar-escola.html', {'escolas': escolas})

def adicionarEscola(request):
    form = EscolaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listarEscola')

    return render(request, 'escola/adicionar-escola.html', {'form': form})

def editarEscola(request, id):
    escola = get_object_or_404(Escola, pk=id)
    form = EscolaForm(request.POST or None, instance=escola)

    if form.is_valid():
        form.save()
        return redirect('listarEscola')

    return render(request, 'escola/editar-escola.html', {'form': form})

def excluirEscola(request, id):
    escola = get_object_or_404(Escola, pk=id)

    if request.method == 'POST':
        escola.delete()
        return redirect('listarEscola')

    return render(request, 'escola/excluir-escola.html', {'escola': escola})

#funções da entidade Turma
def listarTurma(request):
    nome = request.GET.get('nome', None)

    turmas = Turma.objects.all()

    return render(request, 'turma/listar-turma.html', {'turmas': turmas})

def adicionarTurma(request):
    form = TurmaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listarTurma')

    return render(request, 'turma/adicionar-turma.html', {'form': form})

def editarTurma(request, id):
    turma = get_object_or_404(Turma, pk=id)
    form = TurmaForm(request.POST or None, instance=turma)

    if form.is_valid():
        form.save()
        return redirect('listarTurma')

    return render(request, 'turma/editar-turma.html', {'form': form})

def excluirTurma(request, id):
    turma = get_object_or_404(Turma, pk=id)

    if request.method == 'POST':
        turma.delete()
        return redirect('listarTurma')

    return render(request, 'turma/excluir-turma.html', {'turma': turma})

#funções da entidade Aluno
def listarAluno(request):
    nome = request.GET.get('nome', None)

    alunos = Aluno.objects.all()

    return render(request, 'aluno/listar-aluno.html', {'alunos': alunos})

def adicionarAluno(request):
    form = AlunoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listarAluno')

    return render(request, 'aluno/adicionar-aluno.html', {'form': form})

def editarAluno(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    form = AlunoForm(request.POST or None, instance=aluno)

    if form.is_valid():
        form.save()
        return redirect('listarAluno')

    return render(request, 'aluno/editar-aluno.html', {'form': form})

def excluirAluno(request, id):
    aluno = get_object_or_404(Aluno, pk=id)

    if request.method == 'POST':
        aluno.delete()
        return redirect('listarAluno')

    return render(request, 'aluno/excluir-aluno.html', {'aluno': aluno})

#funções da entidade Professor
def listarProfessor(request):
    nome = request.GET.get('nome', None)

    professores = Professor.objects.all()

    return render(request, 'professor/listar-professor.html', {'professores': professores})

def adicionarProfessor(request):
    form = ProfessorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listarProfessor')

    return render(request, 'professor/adicionar-professor.html', {'form': form})

def editarProfessor(request, id):
    professor = get_object_or_404(Professor, pk=id)
    form = ProfessorForm(request.POST or None, instance=professor)

    if form.is_valid():
        form.save()
        return redirect('listarProfessor')

    return render(request, 'professor/editar-professor.html', {'form': form})

def excluirProfessor(request, id):
    professor = get_object_or_404(Professor, pk=id)

    if request.method == 'POST':
        professor.delete()
        return redirect('listarProfessor')

    return render(request, 'professor/excluir-professor.html', {'professor': professor})

#funções da entidade Disciplina
def listarDisciplina(request):
    nome = request.GET.get('nome', None)

    disciplinas = Disciplina.objects.all()

    return render(request, 'disciplina/listar-disciplina.html', {'disciplinas': disciplinas})

def adicionarDisciplina(request):
    form = DisciplinaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listarDisciplina')

    return render(request, 'disciplina/adicionar-disciplina.html', {'form': form})

def editarDisciplina(request, id):
    disciplina = get_object_or_404(Disciplina, pk=id)
    form = DisciplinaForm(request.POST or None, instance=disciplina)

    if form.is_valid():
        form.save()
        return redirect('listarDisciplina')

    return render(request, 'disciplina/editar-disciplina.html', {'form': form})

def excluirDisciplina(request, id):
    disciplina = get_object_or_404(Disciplina, pk=id)

    if request.method == 'POST':
        disciplina.delete()
        return redirect('listarDisciplina')

    return render(request, 'disciplina/excluir-disciplina.html', {'disciplina': disciplina})

#funções da entidade Habilidade
def listarHabilidade(request):
    nome = request.GET.get('nome', None)

    habilidades = Habilidade.objects.all()

    return render(request, 'habilidade/listar-habilidade.html', {'habilidades': habilidades})

def adicionarHabilidade(request):
    form = HabilidadeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listarHabilidade')

    return render(request, 'habilidade/adicionar-habilidade.html', {'form': form})

def editarHabilidade(request, id):
    habilidade = get_object_or_404(Habilidade, pk=id)
    form = HabilidadeForm(request.POST or None, instance=habilidade)

    if form.is_valid():
        form.save()
        return redirect('listarHabilidade')

    return render(request, 'habilidade/editar-habilidade.html', {'form': form})

def excluirHabilidade(request, id):
    habilidade = get_object_or_404(Habilidade, pk=id)

    if request.method == 'POST':
        habilidade.delete()
        return redirect('listarHabilidade')

    return render(request, 'habilidade/excluir-habilidade.html', {'habilidade': habilidade})

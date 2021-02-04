from django.shortcuts import render, redirect, get_object_or_404
from .models import Escola, Turma, Aluno, Professor, Disciplina, Habilidade, Matricula, Contem, Promove, Ministra

from .forms import EscolaForm, TurmaForm, AlunoForm, ProfessorForm, DisciplinaForm, HabilidadeForm, MatriculaForm, ContemForm, PromoveForm, MinistraForm

# Create your views here.
#funções da entidade Escola
def listarEscola(request):
    codigo = request.GET.get('codigo', None)

    if codigo:
        escolas = Escola.objects.filter(id__icontains=codigo)
    else:
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
    codigo = request.GET.get('codigo', None)

    if codigo:
        turmas = Turma.objects.filter(id__icontains=codigo)
    else:
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
    codigo = request.GET.get('codigo', None)
    
    if codigo:
        alunos = Aluno.objects.filter(id__icontains=codigo)
    else:
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
    codigo = request.GET.get('codigo', None)

    if codigo:
        professores = Professor.objects.filter(id__icontains=codigo)
    else:
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
    codigo = request.GET.get('codigo', None)
    
    if codigo:
        disciplinas = Disciplina.objects.filter(id__icontains=codigo)
    else:
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
    codigo = request.GET.get('codigo', None)

    if codigo:
        habilidades = Habilidade.objects.filter(id__icontains=codigo)
    else:
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

#funções da entidade Matricula que é a tabela da relação entre (Aluno e Turma)
def listarMatricula(request):
    codigo = request.GET.get('codigo', None)

    if codigo:
        matriculas = Matricula.objects.filter(id__icontains=codigo)
    else:
        matriculas = Matricula.objects.all()

    return render(request, 'matricula/listar-matricula.html', {'matriculas': matriculas})

def adicionarMatricula(request):
    form = MatriculaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listarMatricula')

    return render(request, 'matricula/adicionar-matricula.html', {'form': form})

def editarMatricula(request, id):
    matricula = get_object_or_404(Matricula, pk=id)
    form = MatriculaForm(request.POST or None, instance=matricula)

    if form.is_valid():
        form.save()
        return redirect('listarMatricula')

    return render(request, 'matricula/editar-matricula.html', {'form': form})

def excluirMatricula(request, id):
    matricula = get_object_or_404(Matricula, pk=id)

    if request.method == 'POST':
        matricula.delete()
        return redirect('listarMatricula')

    return render(request, 'matricula/excluir-matricula.html', {'matricula': matricula})

#funções da entidade Contem que é a tabela da relação entre (Turma e Disciplina)
def listarContem(request):
    codigo = request.GET.get('codigo', None)

    if codigo:
        contens = Contem.objects.filter(id__icontains=codigo)
    else:
        contens = Contem.objects.all()

    return render(request, 'contem/listar-contem.html', {'contens': contens})

def adicionarContem(request):
    form = ContemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listarContem')

    return render(request, 'contem/adicionar-contem.html', {'form': form})

def editarContem(request, id):
    contem = get_object_or_404(Contem, pk=id)
    form = ContemForm(request.POST or None, instance=contem)

    if form.is_valid():
        form.save()
        return redirect('listarContem')

    return render(request, 'contem/editar-contem.html', {'form': form})

def excluirContem(request, id):
    contem = get_object_or_404(Contem, pk=id)

    if request.method == 'POST':
        contem.delete()
        return redirect('listarContem')

    return render(request, 'contem/excluir-contem.html', {'contem': contem})

#funções da entidade Promove que é a tabela da relação entre (Disciplina e Habilidade)
def listarPromove(request):
    codigo = request.GET.get('codigo', None)

    if codigo:
        promoves = Promove.objects.filter(id__icontains=codigo)
    else:
        promoves = Promove.objects.all()

    return render(request, 'promove/listar-promove.html', {'promoves': promoves})

def listarHabilidadesNecessariasDeUmaDisciplina(request, id):
    codigo = id

    if codigo:
        promoves = Promove.objects.filter(codigoDisciplina_id__exact=codigo)
    else:
        promoves = []

    return render(request, 'promove/listar-habilidades-necessarias.html', {'promoves': promoves})

def adicionarPromove(request):
    form = PromoveForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listarPromove')

    return render(request, 'promove/adicionar-promove.html', {'form': form})

def editarPromove(request, id):
    promove = get_object_or_404(Promove, pk=id)
    form = PromoveForm(request.POST or None, instance=promove)

    if form.is_valid():
        form.save()
        return redirect('listarPromove')

    return render(request, 'promove/editar-promove.html', {'form': form})

def excluirPromove(request, id):
    promove = get_object_or_404(Promove, pk=id)

    if request.method == 'POST':
        promove.delete()
        return redirect('listarPromove')

    return render(request, 'promove/excluir-promove.html', {'promove': promove})

#funções da entidade Ministra que é a tabela da relação entre (Professor e Disciplina)
def listarMinistra(request):
    codigo = request.GET.get('codigo', None)

    if codigo:
        ministras = Ministra.objects.filter(id__icontains=codigo)
    else:
        ministras = Ministra.objects.all()

    return render(request, 'ministra/listar-ministra.html', {'ministras': ministras})

def adicionarMinistra(request):
    form = MinistraForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listarMinistra')

    return render(request, 'ministra/adicionar-ministra.html', {'form': form})

def editarMinistra(request, id):
    ministra = get_object_or_404(Ministra, pk=id)
    form = MinistraForm(request.POST or None, instance=ministra)

    if form.is_valid():
        form.save()
        return redirect('listarMinistra')

    return render(request, 'ministra/editar-ministra.html', {'form': form})

def excluirMinistra(request, id):
    ministra = get_object_or_404(Ministra, pk=id)

    if request.method == 'POST':
        ministra.delete()
        return redirect('listarMinistra')

    return render(request, 'ministra/excluir-ministra.html', {'ministra': ministra})

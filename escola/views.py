from django.shortcuts import render, redirect, get_object_or_404
from .models import Escola
from .forms import EscolaForm

# Create your views here.
def listarEscola(request):
    nome = request.GET.get('nome', None)

    escolas = Escola.objects.all()

    return render(request, 'lista-escola.html', {'escolas': escolas})


def adicionarEscola(request):
    form = EscolaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listarEscola')

    return render(request, 'adiciona-escola.html', {'form': form})


def editarEscola(request, id):
    escola = get_object_or_404(Escola, pk=id)
    form = EscolaForm(request.POST or None, instance=escola)

    if form.is_valid():
        form.save()
        return redirect('listarEscola')

    return render(request, 'editar-escola.html', {'form': form})


def excluirEscola(request, id):
    escola = get_object_or_404(Escola, pk=id)

    if request.method == 'POST':
        escola.delete()
        return redirect('listarEscola')

    return render(request, 'excluir-escola.html', {'escola': escola})
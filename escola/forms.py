from django.forms import ModelForm
from .models import Escola

class EscolaForm(ModelForm):
    class Meta:
        model = Escola
        fields = ['nome', 'descricao', 'telefone', 'email']
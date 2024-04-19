from django import forms
from .models import Servico, OrdemServico
from geral.models import Mecanico, Oficina

class ServicoForm(forms.ModelForm):
        class Meta:
            model = Servico
            exclude = ['oficina']

class OrdemdeServicoForm(forms.ModelForm):
        class Meta:
            model = OrdemServico
            exclude = ['oficina']

        def __init__(self, *args, **kwargs):
            request = kwargs.pop('request', None)
            super().__init__(*args, **kwargs)
            if request:
                usuario = request.user
                oficina = Oficina.objects.get(usuario=usuario)
                self.fields['mecanico'].queryset = Mecanico.objects.filter(oficina=oficina)                
                self.fields['servico'].queryset = Servico.objects.filter(oficina=oficina)
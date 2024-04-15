from django.shortcuts import render, redirect, get_object_or_404
from .forms import ServicoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Servico
from servicos.models import Oficina

# Create your views here.
@login_required
def novo_servico(request):
    template_name = 'servicos/novo_servico.html'
    context = {}
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            of = form.save(commit=False)
            usuario = request.user
            oficina = Oficina.objects.get(usuario=usuario)
            of.oficina = oficina
            of.save()
            messages.success(request, 'Serviço cadastrado com sucesso!')
            return redirect('servicos:lista_servicos')
    else:
        form = ServicoForm()
    
    context['form'] = form    
    return render(request, template_name, context)

@login_required
def lista_servicos(request):
    template_name = 'servicos/lista_servicos.html' 
    oficinas = Oficina.objects.filter(usuario=request.user)         
    servicos = Servico.objects.filter(oficina__in=oficinas)
    context = {
        'servicos': servicos,
    }
    return render(request, template_name, context)


@login_required
def apagar_servicos(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    servico.delete()
    messages.info(request, 'Serviço excluído com sucesso!')
    return redirect('servicos:lista_servicos')

@login_required
def editar_servico(request, pk):
    template_name = 'servicos/novo_servico.html'
    context = {

    }
    servico = get_object_or_404(Servico, pk=pk)
    if request.method == 'POST':
        form = ServicoForm(data=request.POST, instance=servico)
        form.save()
        messages.success(request, 'Serviço atualizado com sucesso!')
        return redirect('servicos:lista_servicos')
    form = ServicoForm(instance=servico)    
    context['form'] = form    
    return render(request, template_name, context)
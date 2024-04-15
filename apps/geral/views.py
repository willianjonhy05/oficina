from django.shortcuts import render, redirect, get_object_or_404
from .forms import OficinaForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Oficina

@login_required
def home(request):
    template_name = 'geral/home.html'
    context = {}
    return render(request, template_name, context)



@login_required
def nova_oficina(request):
    template_name = 'geral/nova_oficina.html'
    context = {}
    if request.method == 'POST':
        form = OficinaForm(request.POST)
        if form.is_valid():
            of = form.save(commit=False)
            of.usuario = request.user
            of.save()
            messages.success(request, 'Oficina cadastrada com sucesso!')
            return redirect('geral:lista_oficina')
        
    form = OficinaForm()    
    context['form'] = form    
    return render(request, template_name, context)


@login_required
def lista_oficina(request):
    template_name = 'geral/lista_oficina.html'
    oficinas = Oficina.objects.filter(usuario=request.user)
    context = {
        'oficinas': oficinas,
    }
    return render(request, template_name, context)



# @login_required
# def apagar_oficina(request, id):
#     oficina = Oficina.objects.get(usuario=request.user, id=id)    
#     oficina.delete()
#     return redirect('geral:lista_oficina')

@login_required
def apagar_oficina(request, pk):
    oficina = get_object_or_404(Oficina, pk=pk)
    oficina.delete()
    messages.info(request, 'Oficina excluída com sucesso!')
    return redirect('geral:lista_oficina')


@login_required
def editar_oficina(request, pk):
    template_name = 'geral/nova_oficina.html'
    context = {

    }
    oficina = get_object_or_404(Oficina, pk=pk)
    if request.method == 'POST':
        form = OficinaForm(data=request.POST, instance=oficina)
        form.save()
        messages.success(request, 'Oficina atualizada com sucesso!')
        return redirect('geral:lista_oficina')
    form = OficinaForm(instance=oficina)
    status = 'Salvar'
    context['form'] = form
    context['Salvar'] = status
    return render(request, template_name, context)
    


# @login_required
# def atualizar_oficina(request, pk):
#     template_name = 'geral/nova_oficina.html'
#     oficina = Oficina.objects.get(usuario=request.user, id=id)
#     forms = OficinaForm(instance=oficina)
#     context = {
#         'forms': forms,
#     }
#     if request.method == "POST":
#     return render(request, template_name, context)
from django.shortcuts import render, redirect
from .forms import OficinaForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Oficina


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


def lista_oficina(request):
    template_name = 'geral/lista_oficina.html'
    oficinas = Oficina.objects.filter(usuario=request.user)
    context = {
        'oficinas': oficinas,
    }
    return render(request, template_name, context)




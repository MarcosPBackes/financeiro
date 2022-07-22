from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import VariavelForm
from .models import Variavel
def carteiras(request):
    return render(request, 'carteiras/carteira.html')

def variavel_list(request):
    variavel_list = Variavel.objects.all().order_by('-created_at').filter(user=request.user)
    
    paginator = Paginator(variavel_list, 10)
    
    page = request.GET.get('page')
    
    variavel = paginator.get_page(page)
    
    return render(request, 'carteiras/variavel_list.html',
                  {'variavel': variavel})

def variavel_view(request, id):
   variavel = get_object_or_404(Variavel, pk=id)
   return render(request, 'carteiras/variavel_view.html',
                 {'variavel': variavel})

def variavel_add(request):
    if request.method == 'POST':
        form = VariavelForm(request.POST)
        
        if form.is_valid():
            variavel = form.save(commit=False)
            variavel.user = request.user
            variavel.save()
            return redirect('variavel_list')
        else:
            form = VariavelForm()
            return render(request, 'carteiras/variavel_add.htlm',
                          {'form': form})

def variavel_edit(request, id):
    variavel = get_object_or_404(Variavel, pk=id)
    form = VariavelForm(instace=variavel)
    
    if(request.method == 'POST'):
        form = VariavelForm(request.POST, instance=variavel)
        if(form.is_valid()):
            variavel.save()
            return redirect('variavel_list')
        else:
            return render(request, 'carteiras/variavel_edit.html',
                          {'form':form, 'variavel':variavel})
            
def variavel_delete(request, id):
    variavel = get_object_or_404(Variavel, pk=id)
    variavel.delete()
    
    messages.info(request, 'Deletada com sucesso!')
    
    return redirect('variavel_list')


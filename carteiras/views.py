from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import VariavelForm
from .models import Variavel

def variavel_list(request):
    acao_list = Variavel.objects.all().order_by('-created_at').filter(user=request.user)
    
    paginator = Paginator(acao_list, 10)
    
    page = request.GET.get('page')
    
    acao = paginator.get_page(page)
    
    return render(request, 'carteira/variavel.html', {'acao': acao})

def variavel_view(request, id):
    
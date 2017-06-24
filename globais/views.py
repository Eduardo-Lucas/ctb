from django.shortcuts import render

from .forms import GlobEmpresasForm

# Create your views here.


def empresalista(request):
    return render(request, 'empresa/empresaLista.html')


def empresaadiciona(request):
    if request.method == "POST":
        form = GlobEmpresasForm(request.POST)
    else:
        form = GlobEmpresasForm()

    return render(request, 'empresa/empresaAdiciona.html', {'form': form})


def empresaedita(request):
    return render(request, 'empresa/empresaEdita.html')

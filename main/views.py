from django.shortcuts import render,redirect
from .forms import FormulirForm
from django.contrib import messages
# Create your views here.
def show_main(request):
    context = {
    }
    return render(request, 'main.html', context)

def formulir(request):
    if request.method == 'POST':
        form = FormulirForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Informasimu telah berhasil dikirim')
            return redirect('main:show_main')
    else:
        form = FormulirForm()

    
    context = {'form':form}
    
    return render(request, 'formulir.html', context)
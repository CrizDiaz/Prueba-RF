from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.mascota.forms import MascotaForm
from apps.mascota.models import mascota


# Create your views here.

def index(request):
    return render(request, 'mascota/index.html')

### Vista basada en funcion ###
def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mascota_listar') #index
    else:
        form = MascotaForm()    
    return render(request, 'mascota/mascota_form.html', {'form':form})

### Vista basada en funcion ###
def mascota_list(request):
    Mascota = mascota.objects.all().order_by('id')
    contexto = {'mascotas':Mascota}
    return render(request, 'mascota/mascota_list.html', contexto)

def mascota_edit(request, id_mascota):
    Mascota = mascota.objects.get(id=id_mascota)
    if request.method == 'GET':
        form = MascotaForm(instance=Mascota)
    else:
        form = MascotaForm(request.POST, instance=Mascota)
        if form.is_valid():
            form.save()
        return redirect('mascota_listar')
    return render(request, 'mascota/mascota_form.html', {'form':form})

def mascota_delete(request, id_mascota):
    Mascota = mascota.objects.get(id=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascota_listar')
    return render(request,'mascota/mascota_delete.html',{'mascota':mascota})

### Vista basada en clase (ListView) ###
class MascotaList(ListView):
    model = mascota
    template_name = 'mascota/mascota_list.html'

### Vista basada en clase (CreateView) ###
class MascotaCreate(CreateView):
    model = mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'    
    success_url = reverse_lazy('mascota_listar')

class MascotaUpdate(UpdateView):
    model = mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota_listar')

class MascotaDelete(DeleteView):
    model = mascota
    template_name = 'mascota/mascota_delete.html'
    success_url = reverse_lazy('mascota_listar')
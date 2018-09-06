from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from core.models import Proyecto, Desarrollo
from core.forms import ProyectoForm, DesarrolloForm

import itertools
import string

from django.db.models import Max

# Create your views here.
def index(request):
    return render(request, 'core/index.html')


class ProyectoListView(ListView):
    model = Proyecto
    paginate_by = 10
    template_name = 'core/proyecto_list.html'


class ProyectoDetailView(DetailView):
    model = Proyecto


class ProyectoCreate(CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'core/proyecto_form.html'
    success_url = reverse_lazy('proyectos')


class DesarrolloCreate(CreateView):
    model = Desarrollo
    form_class = DesarrolloForm
    template_name = 'core/desarrollo_form.html'     

    def get_initial(self):
        initials = super(DesarrolloCreate, self).get_initial()
        initials['proyecto'] = self.kwargs['proyecto_id']
        a= list(map('.'.join, itertools.product(string.digits, repeat=4)))
        b = Desarrollo.objects.filter(proyecto_id=self.kwargs['proyecto_id']).first()
        if b is None:
            b = Desarrollo()
            b.version = '1.0.0.0'
        c = b.version
        d = c.replace('.', '')
        initials['version'] = a[int(d)+1]
        return initials

    def get_success_url(self):
        return reverse_lazy('proyecto-detail', kwargs={'pk': self.kwargs['proyecto_id']})


class ProyectoUpdate(UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'core/proyecto_form.html'
    #success_url = reverse_lazy('proyectos')

    def get_absolute_url(self):
        return reverse('proyecto_busqueda', kwargs={'nombre': self.nombre})


class DesarrolloUpdate(UpdateView):
    model = Desarrollo
    form_class = DesarrolloForm
    template_name = 'core/desarrollo_form.html'
    
    def get_success_url(self):
        return reverse_lazy('proyecto-detail', kwargs={'pk': self.get_object().proyecto_id})


class ProyectoDelete(DeleteView):
    model = Proyecto
    template_name = 'core/proyecto_delete'
    success_url = reverse_lazy('proyectos')


class DesarrolloDelete(DeleteView):
    model = Desarrollo
    template_name = 'core/desarrollo_delete.html'

    def get_success_url(self):
        return reverse_lazy('proyecto-detail', kwargs={'pk': self.get_object().proyecto_id})


def busqueda(request):
   q = request.GET.get('q','')
   proyectos = Proyecto.objects.filter(nombre__icontains=q)
   return render(request, 'core/proyecto_busqueda.html', {'proyectos': proyectos})

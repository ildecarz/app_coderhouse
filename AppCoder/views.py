from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from AppCoder.models import (
    Curso,
)


def home(request):
    return render(request,'AppCoder/app_home.html')


class CursosListView(ListView):
    model = Curso
    template_name = 'AppCoder/curso_listview.html' # <app>/<model>_<wietype>.html
    context_object_name = 'cursos'
    paginate_by = 5

class CursosDetailView(DetailView):
    model = Curso

class CursosCreateView(CreateView):
    model = Curso
    success_url = '/'
    fields = ['nombre', 'camada']


class CursosUpdateView(UpdateView):
    model = Curso
    fields = ['nombre', 'camada']
    success_url = '/'


class CursosDeleteView(DeleteView):
    model = Curso
    success_url = '/'
    


def about(request):
    return render(request,'AppCoder/about.html')




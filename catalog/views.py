from dataclasses import fields
from django.shortcuts import render

from .models import Group
from .models import Note

from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from catalog.forms import GroupForm, NoteBodyForm, NoteBodyForm_new

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

@login_required
def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_groups=Group.objects.all().count()
    num_notes=Note.objects.all().count()
    group2=Group.objects.filter(groupName__startswith='П')
    
    form = GroupForm()

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_groups':num_groups,'num_notes':num_notes, 'group2':group2, 'form':form},
    )

class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['groupID', 'article', 'noteBody']
    
    def post(self, request, *args, **kwargs):
        # note_instance = get_object_or_404(Note, pk=pk)
        # form = NoteBodyForm()
        if request.method == "POST" and request.POST.get("groups") is not None:
            form = NoteBodyForm(request.POST)
            if form.is_valid:
         #redirect to the url where you'll process the input
                # Note.groupID = request.POST.get("groups")
                # Note.article = request.POST.get("article")
                # Note.noteBody = request.POST.get("noteBody")
                # Note.save()
                n = Note(
                    # groupID = Group(id = request.POST.get("groups")), # Вариант1 как получить экземпляр объекта по id
                    groupID = Group.objects.get(id = request.POST.get("groups")),  # Вариант2 как получить экземпляр объекта по id
                    article = request.POST.get("article"), 
                    noteBody =  request.POST.get("noteBody"))
                n.save()
                return render(request, 'catalog/note_form.html',{'form': form})
        return super(NoteCreate, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(NoteCreate, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и инициализируем её некоторым значением
        form = NoteBodyForm()
        context['form'] = form
        return context

    # initial = {'date_of_death': '11/06/2020'}

class NoteUpdate(LoginRequiredMixin, UpdateView):
    model = Note
    # fields = ['groupID','article', 'noteBody'] # Not recommended (potential security issue if more fields added)

    template_name = 'catalog/note_update.html'
    form_class = NoteBodyForm_new

class NoteDelete(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('note')

class GroupCreate(LoginRequiredMixin, CreateView):
    model = Group
    fields = ['groupName']

class GroupUpdate(LoginRequiredMixin, UpdateView):
    model = Group
    fields = ['groupName'] # Not recommended (potential security issue if more fields added)

class GroupDelete(LoginRequiredMixin, DeleteView):
    model = Group
    success_url = reverse_lazy('group')

class GroupListView(LoginRequiredMixin, generic.ListView):
    model = Group
    paginate_by = 10

class NoteListView(LoginRequiredMixin, generic.ListView):
    model = Note
    
    def get(self, request, *args, **kwargs):
        form = GroupForm()
        if request.method == "GET" and request.GET.get("groups") is not None:
            form = GroupForm(request.GET)
            if form.is_valid:
         #redirect to the url where you'll process the input
                gr=request.GET.get("groups")
                note_list=Note.objects.filter(groupID=gr)
                return render(request, 'catalog/note_list.html',{'form': form,'note_list':note_list})
        return super(NoteListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(NoteListView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и инициализируем её некоторым значением
        form = GroupForm()
        context['form'] = form
        return context
        
    paginate_by = 10

class NoteDetailView(LoginRequiredMixin, generic.DetailView):
    model = Note

class GroupDetailView(LoginRequiredMixin, generic.DetailView):
    model = Group
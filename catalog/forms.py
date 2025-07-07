from django import forms
from .models import Group
from .models import Note
from django.forms import ModelForm, Textarea, TextInput, Select

class RenewNoteForm(forms.Form):
    renewal_noteBody = forms.CharField(help_text="Enter a text of note")

class GroupForm(forms.Form):
    groups = forms.ModelChoiceField(queryset=Group.objects.all().order_by('groupName'), label='')

class NoteBodyForm(forms.Form):
    groups = forms.ModelChoiceField(queryset=Group.objects.all().order_by('groupName'))
    article = forms.CharField()
    noteBody = forms.CharField(widget=forms.Textarea(attrs={'cols':'70', 'rows':'20'}))

class NoteBodyForm_new(ModelForm):
    class Meta:
        model = Note
        fields = ['groupID', 'article', 'noteBody']
    
        widgets = {
            "groupID": Select(attrs = {
                # 'style': 'width: 400px;',
            }),
            "article": TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Заголовок'
            }), 
            "noteBody": Textarea(attrs = {
                'class': 'form-control',
                'rows': '10',
                'placeholder': 'Текст заметки'
            })
        }
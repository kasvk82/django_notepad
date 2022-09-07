from django import forms
from .models import Group

class RenewNoteForm(forms.Form):
    renewal_noteBody = forms.CharField(help_text="Enter a text of note")

class GroupForm(forms.Form):
    groups = forms.ModelChoiceField(queryset=Group.objects.all().order_by('groupName'))
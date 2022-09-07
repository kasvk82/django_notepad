from django.contrib import admin
from .models import Group, Note

# class NoteInLine(admin.TabularInline):
#     model = Note

class GroupAdmin(admin.ModelAdmin):
    pass
    #inlines = [NoteInLine]

admin.site.register(Group, GroupAdmin)

# Register your models here.
#admin.site.register(Group)
#admin.site.register(Note)

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('creationDateTime', 'article', 'groupID')
    list_filter = ('groupID', 'article')

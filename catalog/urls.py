from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.index, name='index'),
    # path('', RedirectView.as_view(url='group/', permanent=True)),
    path('group/', views.GroupListView.as_view(), name='group'),
    path('note/', views.NoteListView.as_view(), name='note'),
    path('note/<int:pk>', views.NoteDetailView.as_view(), name='note-detail'),
    path('group/<uuid:pk>', views.GroupDetailView.as_view(), name='group-detail'),
    path('note/create/', views.NoteCreate.as_view(), name='note-create'),
    # path('note/filterbygroup', views.show_group, name='show_group'),
    path('group/create/', views.GroupCreate.as_view(), name='group-create'),
    path('note/<int:pk>/update/', views.NoteUpdate.as_view(), name='note-update'),
    path('note/<int:pk>/delete/', views.NoteDelete.as_view(), name='note-delete'),
    path('group/<uuid:pk>/update/', views.GroupUpdate.as_view(), name='group-update'),
    path('group/<uuid:pk>/delete/', views.GroupDelete.as_view(), name='group-delete'),
]
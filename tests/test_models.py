from django.test import TestCase

from catalog.models import Group
from catalog.models import Note

class GroupModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Group.objects.create(groupName='Main')

    def test_group_name_label(self):
        group = Group.objects.get(groupName="Main")
        field_label = group._meta.get_field('groupName').verbose_name
        self.assertEqual(field_label, 'groupName')

    def test_group_name_max_length(self):
        group = Group.objects.get(groupName="Main")
        max_length = group._meta.get_field('groupName').max_length
        self.assertEqual(max_length, 28)

    def test_get_absolute_url(self):
        group = Group.objects.get(groupName="Main")
        id_group = group.id
        # This will also fail if the urlconf is not defined.
        self.assertEqual(group.get_absolute_url(), f'/catalog/group/{id_group}')

class NoteModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Group.objects.create(groupName='Main')
        Note.objects.create(article='test', noteBody='test_test', groupID=Group.objects.get(groupName='Main'))

    def test_creationDateTime_label(self):
        note = Note.objects.get(id=1)
        field_label = note._meta.get_field('creationDateTime').verbose_name
        self.assertEqual(field_label, 'creationDateTime')

    def test_article_max_length(self):
        note = Note.objects.get(id=1)
        max_length = note._meta.get_field('article').max_length
        self.assertEqual(max_length, 128)
    
    def test_noteBody_max_length(self):
        note = Note.objects.get(id=1)
        max_length = note._meta.get_field('noteBody').max_length
        self.assertEqual(max_length, 2000)

    def test_get_absolute_url(self):
        note = Note.objects.get(id=1)
        # id_group = group.id
        # This will also fail if the urlconf is not defined.
        self.assertEqual(note.get_absolute_url(), '/catalog/note/1')
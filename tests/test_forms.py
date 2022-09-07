import datetime

from django.test import TestCase
from django.utils import timezone

from catalog.forms import GroupForm

class GroupFormTest(TestCase):
    def test_group_form_date_field_label(self):
        form = GroupForm()
        self.assertTrue(form.fields['groups'].label is None or form.fields['groups'].label == 'groups')
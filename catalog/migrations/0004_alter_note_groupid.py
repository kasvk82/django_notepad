# Generated by Django 5.1.3 on 2025-06-22 03:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20211020_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='groupID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.group', verbose_name='Group'),
        ),
    ]

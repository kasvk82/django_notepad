# Generated by Django 3.2.8 on 2021-10-20 16:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Identification of Group', primary_key=True, serialize=False)),
                ('groupName', models.CharField(help_text='Group name', max_length=28)),
            ],
            options={
                'ordering': ['groupName'],
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Identification of Note', primary_key=True, serialize=False)),
                ('noteName', models.CharField(help_text='Note name', max_length=64)),
                ('creationDateTime', models.DateTimeField(auto_now=True, help_text='Creation Date')),
                ('groupID', models.ForeignKey(help_text='Group name', on_delete=django.db.models.deletion.PROTECT, to='catalog.group')),
            ],
            options={
                'ordering': ['creationDateTime'],
            },
        ),
        migrations.CreateModel(
            name='NoteContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.CharField(help_text='Article', max_length=128)),
                ('noteBody', models.TextField(help_text='Text', max_length=1000)),
                ('noteID', models.OneToOneField(help_text='Identification of NoteContent', on_delete=django.db.models.deletion.CASCADE, to='catalog.note')),
            ],
            options={
                'ordering': ['noteID'],
            },
        ),
    ]

from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique Group and Note instances

# Create your models here.
class Group(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Identification of Group')
    groupName = models.CharField(max_length=28, help_text='Group name')

    # Metadata
    class Meta:
        ordering = ['groupName']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of Group."""
        return reverse('group-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Group                         ect (in Admin site etc.)."""
        return self.groupName
    
    def get_val(self):
        self.sVal = 1
        return self.sVal
    
class Note(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    #id =  models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Identification of Note')
    groupID = models.ForeignKey(Group, on_delete=models.PROTECT, help_text='Group name')
    creationDateTime = models.DateTimeField(auto_now=True, help_text='Creation Date')
    article = models.CharField(max_length=128, null=True, help_text='Article')
    noteBody = models.TextField(max_length=2000, null=True, help_text='Text')

    # Metadata
    class Meta:
        ordering = ['article']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of Note."""
        return reverse('note-detail', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the Note object (in Admin site etc.)."""
        return self.article
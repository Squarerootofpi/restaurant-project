from django.db import models

# Create your models here.


class Restaurant(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    name = models.CharField(max_length=20, help_text='Enter field documentation')
    cost = models.CharField(max_length=100, null=True)
    cuisine = models.CharField(max_length=100, null=True)
    health_factor = models.CharField(max_length=100, null=True)
    wait_time = models.IntegerField(null=True)
    travel_time = models.IntegerField(null=True)    
    drive_through = models.BooleanField(null=True)

    # Metadata
    class Meta: 
        ordering = ['-name']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name

class RecommendationsForm(models.Model):
    cost = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    health_factor = models.CharField(max_length=100)
    wait_time = models.IntegerField(null=True)
    travel_time = models.IntegerField(null=True)    
    drive_through = models.BooleanField(null=True)

    def __str__(self):
        return self.cost
    
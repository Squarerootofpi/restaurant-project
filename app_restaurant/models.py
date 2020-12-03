from django.db import models

# Create your models here.


class Restaurant(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    name = models.CharField(max_length=45, help_text='Enter field documentation')
    cuisine1 = models.CharField(max_length=100, null=True)
    cuisine2 = models.CharField(max_length=100, null=True)
    cuisine3 = models.CharField(max_length=100, null=True)
    price_range = models.CharField(max_length=100, null=True)
    rating= models.CharField(max_length=100, null=True)

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


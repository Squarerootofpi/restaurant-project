from django.db import models
from enum import Enum

from django.contrib.auth.models import User

# Create your models here.


class Restaurant(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    
    name = models.CharField(max_length=128)
    link = models.URLField('Web Address', blank=True)
    class COST(Enum):
        cheap = ('cheap', 'Cheap')
        moderate = ('moderate', 'moderate')
        expensive = ('expensive', 'Expensive')

        @classmethod
        def get_value(cls, member):
            return member.value[0]
    cost = models.CharField(
        max_length=32,
        choices=[x.value for x in COST],
        default=COST.get_value(COST.moderate),  # OR STATUS.available[0]
    )
    class CUISINE(Enum):
        chinese =('chinese', 'Chinese')
        american = ('american', 'American')
        other = ('other', 'Other Cousine')

        @classmethod
        def get_value(cls, member):
            return member.value[0]
    cuisine = models.CharField(
        max_length=32,
        choices=[x.value for x in CUISINE],
        default=CUISINE.get_value(CUISINE.american),  # OR STATUS.available[0]
    )

    # Metadata

    class Meta: 
        ordering = ['name']
    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name
    # manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

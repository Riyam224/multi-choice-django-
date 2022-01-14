from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.
TYPE_CHOICES = (
		('children' , 'children'),
		('coloring' , 'coloring'),
		('drawing' , 'drawing'),
		('cooking' , 'cooking')

		)
class Book(models.Model):
	
    book_type = MultiSelectField(choices=TYPE_CHOICES)
    image = models.ImageField(upload_to="images" , blank=True , null=True)
    title = models.CharField(max_length=20)
    desc = models.TextField()

    def __str__(self):
    	return self.title
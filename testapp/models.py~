from bootstrap.forms import BootstrapModelForm
from django.forms import ModelForm
from django.db import models
from django import forms

GENDER_CHOICES=(('m','Male'),('f','Female'))
FAVORITE_COLORS_CHOICES = (('blue', 'Blue'),
                            ('green', 'Green'),
                            ('black', 'Black'),
                            ('red','Red'),
                            ('yellow','Yellow'))
                            
                            
class Sample(models.Model):
	name = models.CharField(max_length=100,blank=False)
	address=models.TextField()
	gender= models.CharField(max_length=1, choices=GENDER_CHOICES)
	email=models.EmailField()
	url = models.URLField()
	favorite_colors =  models.CharField(max_length=20, choices=FAVORITE_COLORS_CHOICES)
	color =models.CharField(max_length=20, choices=FAVORITE_COLORS_CHOICES)
	colors =models.CharField(max_length=20, choices=FAVORITE_COLORS_CHOICES)
	upload_file =models.FileField(upload_to='/uploads/')
	
	def __unicode__(self):
		return self.name
	
class SampleForm(BootstrapModelForm):
	class Meta:
		model = Sample
		widgets={
			'gender' : forms.RadioSelect(),
			'favorite_colors' : forms.CheckboxSelectMultiple(),
			'color' : forms.Select(),
			'colors' : forms.SelectMultiple()
			}

# Create your models here.

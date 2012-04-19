from django import forms
#from django.forms.fields import ChoiceField
#from django.forms.widget import RadioSelect
from bootstrap.forms import BootstrapForm, Fieldset

GENDER_CHOICES=(('m','Male'),('f','Female'))
FAVORITE_COLORS_CHOICES = (('blue', 'Blue'),
                            ('green', 'Green'),
                            ('black', 'Black'),
                            ('red','Red'),
                            ('yellow','Yellow'))

class LoginForm(BootstrapForm):
	username=forms.CharField(max_length=100)
	password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"error","placeholder":"Enter Password"}),max_length=100 )
	class Meta:
		layout=(
			Fieldset("Please Login Here","username","password",),
		)
		
class SampleForm(BootstrapForm):
	name = forms.CharField(max_length=100,required=True)
	address=forms.CharField(widget=forms.Textarea)
	gender=forms.ChoiceField(widget = forms.RadioSelect,choices=GENDER_CHOICES)
	email=forms.EmailField(required=True)
	url = forms.URLField(required=True)
	favorite_colors = forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)
	color = forms.ChoiceField(required=False,choices=FAVORITE_COLORS_CHOICES)
	upload_file = forms.FileField(widget=forms.FileInput())
	colors = forms.ChoiceField(required=False,widget=forms.SelectMultiple,choices=FAVORITE_COLORS_CHOICES)
	
		

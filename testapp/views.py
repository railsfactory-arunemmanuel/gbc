# Create your views here.
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from models import SampleForm
from django.shortcuts import render_to_response

def sampleform(request):
	param={}
	errors=[]
	if request.method=='POST':
		form = SampleForm(request.POST)
		if not request.POST['name']:
			errors.append('Please enter name')
		elif len(request.POST['name']) < 10:
			errors.append('Name too short')
		if form.is_valid():
			return HttpResponseRedirect('/sampleform/')
	else:
		form = SampleForm()
	param['form']=form
	param['errors'] = errors
	param.update(csrf(request))
	return render_to_response('sampleform.html',param)

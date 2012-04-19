from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from form import LoginForm,SampleForm
from django.shortcuts import render_to_response

def login(request):
	param={}
	if request.method=="POST":
		form = LoginForm(request.POST)
		if not form.is_valid():
			return HttpResponseRedirect('/login/')
		else:
			return HttpResponseRedirect('/sample/')
	else:
		form = LoginForm()
	param['form']=form
	param.update(csrf(request))
	return render_to_response('login.html',param)
def sample(request):
	param={}
	form = SampleForm()
	param['form']=form
	param.update(csrf(request))
	return render_to_response('login.html',param)

from django.shortcuts import render,redirect

from persons import models
from persons.forms.person import PersonForm

# Create your views here.

def person_list(request):
	obj = models.Person.objects.all()
	return render(request, 'persons/persons_list.html',{'person_obj':obj})


def person_add(request):
	if request.method == 'POST':
		form = PersonForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('persons:person_list')
		else:
			return render(request,'persons/change.html',{'form':form})
	form = PersonForm()
	return render(request,'persons/change.html',{'form':form})


def person_edit(request, pk):
	pass

def person_del(request, pk):
	pass
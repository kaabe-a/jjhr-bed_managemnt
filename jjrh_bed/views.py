from django.shortcuts import render
from . forms import Jjrh_Bed_Form
from . models import BedMnagement

def bed_management_view(request):
	beds = BedMnagement.objects.all()
	context={
		'beds':beds,
	}
	return render(request,'jjrh_bed/bed_manage_view.html',context)

def create_bed_management_view(request):
	if request.method == 'POST':
		form = Jjrh_Bed_Form(request.POST)
		if form.is_valid():
			form.save()
			form = Jjrh_Bed_Form()
	else:
		form  = Jjrh_Bed_Form()
	context = {
		'form':form,
	}
	return render(request,'jjrh_bed/create_bed_management_view.html',context)
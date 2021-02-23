from django.shortcuts import render, get_object_or_404
from . forms import Unitname_Form,Bed_Form
from . models import Bed,UnitName
from django.contrib import messages
from django.db.models import Count,Q

def dashboard(request):
	beds = Bed.objects.all().count()
	unitnames = UnitName.objects.all().count()
	context = {
		'beds':beds,
		'unitnames':unitnames,
	}
	return render(request,'jjrh_bed/dashboard.html',context)
	
	



def view_all(request):
	unitnames = UnitName.objects.annotate(free_beds = Count('id',filter=Q(unitname__status='Free')),
		occupied_beds=Count('id',filter=Q(unitname__status='Occupied')),
		impeding_beds=Count('id',filter=Q(unitname__status='Impeding')), all_beds=Count('id'))
	context = {
		'unitnames':unitnames,
	}
	return render(request,'jjrh_bed/view_all.html',context)

def bed_list_view(request):
	beds = Bed.objects.all()

	# unitnames =	UnitName.objects.annotate(bed_count = Count('bed'))
	# beds = Bed.objects.values('unitname').annotate(num_units = Count('bed_number'))
	# free = Bed.objects.values('unitname').annotate(free_beds = Count('bed_number')).filter(status='Free')
	# occupied = Bed.objects.values('unitname').annotate(occupied_beds = Count('bed_number')).filter(status='Occupied')
	# print(free)
	# print(occupied)

	# beds = Bed.objects.values('unitname').annotate(free_beds=Count('unitname',filter=Q(status="Free")),
	# 	occupied_beds = Count('unitname',filter=Q(status='Occupied')),
	# 	impeding_beds = Count('unitname',filter=Q(status='Impeding')))

	# for bed in beds:
	# 	print(f"{bed['unitname']} | {bed['free_beds']} | {bed['occupied_beds']} | {bed['impeding_beds']} ")

	# unitnames = UnitName.objects.annotate(free_beds = Count('id',filter=Q(unitname__status='Free')),
	# 	occupied_beds=Count('id',filter=Q(unitname__status='Occupied')),
	# 	impeding_beds=Count('id',filter=Q(unitname__status='Impeding')), all_beds=Count('id'))

	# for unitname in unitnames:
		# print(f'{unitname.unit_name} | {unitname.all_beds} | {unitname.free_beds} | {unitname.occupied_beds} | {unitname.impeding_beds}')

	context = {
		'beds':beds,
	}
	return render(request,'jjrh_bed/bed_list_view.html',context)



def bed_management_detail_view(request,id):
	bed = get_object_or_404(Bed,id=id)
	context = {
		'bed':bed,
	}
	return render(request,'jjrh_bed/bed_management_detail_view.html',context)

def bed_update_view(request, id):
	bed = get_object_or_404(Bed, id=id)
	if request.method == 'POST':
		form = Bed_Form(request.POST, instance=bed)
		if form.is_valid():
			form.save()
	else:
		form = Bed_Form(instance=bed)
	context = {
		'form':form,
		'bed':bed,
	}
	return render(request,'jjrh_bed/bed_create_view.html',context)

def bed_delete_view(request, id):
	bed = get_object_or_404(Bed, id=id)
	if request.method == 'POST':
		bed.delete()
	context = {
		'bed':bed,
	}
	return render(request,'jjrh_bed/bed_delete_view_confirm.html',context)


def bed_create_view(request):
	if request.method == 'POST':
		form = Bed_Form(request.POST)
		if form.is_valid():
			form.save()
			form = Bed_Form()
	else:
		form = Bed_Form()
	context = {
		'form':form,
	}
	return render(request,'jjrh_bed/bed_create_view.html',context)


# def bed_management_view(request):
# 	beds = BedMnagement.objects.all()
# 	context={
# 		'beds':beds,
# 	}
# 	return render(request,'jjrh_bed/bed_manage_view.html',context)

def unitname_create_view(request):
	if request.method == 'POST':
		form = Unitname_Form(request.POST)
		if form.is_valid():
			form.save()
			form = Unitname_Form()
	else:
		form  = Unitname_Form()
	context = {
		'form':form,
	}
	return render(request,'jjrh_bed/unitname_create_view.html',context)

def unitname_list_view(request):
	unitnames = UnitName.objects.all()
	context = {
		'unitnames':unitnames,
	}
	return render(request, 'jjrh_bed/unitname_list_view.html',context)

def unitname_detail_view(request,id):
	unitname = get_object_or_404(UnitName,id=id)
	context = {
		'unitname':unitname,
	}
	return render(request, 'jjrh_bed/unitname_detail_view.html',context)

def unitname_update_view(request,id):
	unitname = get_object_or_404(UnitName,id=id)
	if request.method == 'POST':
		form = Unitname_Form(request.POST, instance =unitname)
		if form.is_valid():
			form.save()
			messages.success(request,'You have successfuly created')
		else:
			messages.danger(request,f'{unitname} has been delete successfuly')
	else:
		form = Unitname_Form(instance=unitname)
	context = {
		'form':form,
	}
	return render(request,'jjrh_bed/unitname_create_view.html',context)

def unitname_delete_view(request,id):
	unitname = get_object_or_404(UnitName,id=id)

	if request.method == "POST":
		unitname.delete()
		messages.success(request,f'{unitname} has been delete successfuly')
	context = {
		'unitname':unitname,
	}
	return render(request,'jjrh_bed/unit_delete_view_confirm.html',context)



from django import forms
from . models import Bed,UnitName

class Unitname_Form(forms.ModelForm):
	class Meta:
		model = UnitName
		fields  = "__all__"
		widgets = {
			'Date': forms.DateInput(attrs = {
					'type':'date',
				})
		}

class Bed_Form(forms.ModelForm):
	class Meta:
		model = Bed
		fields = "__all__"
		

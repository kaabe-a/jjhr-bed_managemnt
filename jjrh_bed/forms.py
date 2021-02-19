from django import forms
from . models import BedMnagement
class Jjrh_Bed_Form(forms.ModelForm):
	class Meta:
		model = BedMnagement
		fields  = "__all__"
		widgets = {
			'Date': forms.DateInput(attrs = {
					'type':'date',
				})
		}
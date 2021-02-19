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
		# Date = forms.CharField()
		# Time = forms.CharField()
		# M_A_W_male = CharField()
		# M_A_W_female = CharField()
		# M_B_W_male = CharField()
		# M_B_W_female = CharField()
		# M_C_W_male = CharField()
		# M_C_W_female = CharField()
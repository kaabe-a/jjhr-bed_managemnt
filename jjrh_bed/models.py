from django.db import models
from django.urls import reverse



BED_STATUS_CHOICES = (
        ('Occupied','Occupied'),
        ('Free','Free'),
        ('Impeding','Impeding'),
    )


class UnitName(models.Model):
	Date = models.DateField()
	unit_name = models.CharField(max_length=225)
	# unit_code = models.CharField(max_length=45)
	def __str__(self):
		return self.unit_name


class Bed(models.Model):
	unitname = models.ForeignKey(UnitName,on_delete=models.CASCADE,related_name='unitname')
	bed_number = models.CharField(max_length=56)
	status = models.CharField(
			max_length=34,
			choices=BED_STATUS_CHOICES,
			default='Free',
		)

	def __str__(self):
		return f'{self.bed_number} {self.unitname}'

	def get_absolute_url(self):
		return reverse('jjrh_bed:detail', kwargs={'id':self.id})


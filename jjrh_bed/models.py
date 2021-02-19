from django.db import models

STATUS_CHOICES = (
        ('Morning','Morning'),
        ('Evening','Evening'),
        ('Night','Night'),
    )

class BedMnagement(models.Model):
	Date = models.DateField()
	Time = models.CharField(
			max_length=24,
            choices = STATUS_CHOICES,
            default='Morning',)
	M_A_W_male = models.CharField('Medical ward A Male',max_length=225)
	M_A_W_female = models.CharField('Medical ward A Female',max_length=225)
	M_B_W_male = models.CharField('Medical ward B Male',max_length=225)
	M_B_W_female = models.CharField('Medical ward B Female',max_length=225)
	M_C_W_male = models.CharField('Medical ward C Male',max_length=225)
	M_C_W_female = models.CharField('Medical ward C Female',max_length=225)

	def __str__(self):
		return self.Date, self.Time
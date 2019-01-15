from django.db import models

# Create your models here.
class NatalHoroscope(models.Model):
	permalink = models.CharField(max_length=12,unique=True)
	first_name=models.CharField('First name', max_length=30)
	middle_name=models.CharField('Middle name', max_length=30)
	last_name=models.CharField('Last name', max_length=30)
	date_of_birth=models.DateField('Date of Birth')
	time_of_birth=models.DateTimeField('Time of Birth')
	place_of_birth=models.CharField('Place of Birth', max_length=80)
	current_location=models.CharField('current_location', max_length=80)
	message=models.CharField(max_length=200)
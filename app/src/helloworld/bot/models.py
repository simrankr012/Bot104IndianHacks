from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save

# Create your models here.



class Hospital(models.Model):
	title = models.CharField(max_length=200,null=False, blank=False)
	address = models.CharField(max_length=200,null=False, blank=False) 
	pincode = models.IntegerField(null=False, blank=False)
	contact = models.CharField(max_length=12,null=False, blank=False)
	avg_rating = models.DecimalField(max_digits=3,decimal_places=2,null=False, blank=False,default=0.00)
	disease_speciality = models.CharField(max_length=200,null=False, blank=False,default=None)

	class Meta:
		ordering = ["-avg_rating"]
		verbose_name = 'Hospital'
		verbose_name_plural = "Hospitals"

	def __unicode__(self):
		return str(self.title)

	def __str__(self):
		return str(self.title)



class HospitalBeds(models.Model):
	title = models.ForeignKey(Hospital,on_delete=models.CASCADE)
	is_bed_available = models.BooleanField(default=True)
	room_type_a = models.IntegerField(null=False,blank=False)
	room_type_b = models.IntegerField()


	class Meta:
		ordering = ["is_bed_available"]
		verbose_name = 'Hospital Bed'
		verbose_name_plural = "Hospital Beds"

	def __unicode__(self):
		return str(self.title)

	def __str__(self):
		return str(self.title)


class HospitalRating(models.Model):
	title = models.ForeignKey(Hospital,on_delete=models.CASCADE)
	google_rating = models.DecimalField(max_digits=3,decimal_places=2)
	user_rating = models.IntegerField()


	class Meta:
		verbose_name = 'Hospital Rating'
		verbose_name_plural = 'Hospital Ratings'

	def __unicode__(self):
		return str(self.title)

	def __str__(self):
		return str(self.title)

def hospital_rating_update(sender, instance, **kwargs):
	obj = Hospital.objects.get(title=instance)
	obj.avg_rating = (int(instance.google_rating)+int(instance.user_rating))/2
	print (obj.avg_rating)
	obj.save()

post_save.connect(hospital_rating_update, sender=HospitalRating)



class HospitalBooking(models.Model):
	title = models.ForeignKey(Hospital,on_delete=models.CASCADE)
	bed_type = models.CharField(max_length=2,null=False, blank=False)

	class Meta:
		verbose_name = 'Hospital Booking'
		verbose_name_plural = 'Hospital Bookings'

	def __unicode__(self):
		return str(self.title)

	def __str__(self):
		return str(self.title)



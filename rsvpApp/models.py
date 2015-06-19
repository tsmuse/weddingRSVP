import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class RsvpResponse(models.Model):
	response_date = models.DateTimeField('responded on')

	def pretty_rsvp_name(obj):
		my_name = "RSVP for "
		for guest in obj.guest_set.all():
			my_name += guest.guest_name + ", "	
		return my_name

	def __str__(self):
		return self.pretty_rsvp_name()



class Guest(models.Model):
	rsvp_response = models.ForeignKey(RsvpResponse)
	guest_name = models.CharField(max_length=200)
	guest_attending = models.NullBooleanField()
	drink_choices = ((True, 'Beer'),(False,'Wine'))
	guest_drink_pref = models.BooleanField(choices=drink_choices)


	def pretty_drink_pref(obj):
		pretty_drink = "Wine"
		if obj.guest_drink_pref == True:
			pretty_drink = "Beer"
		return pretty_drink

	def __str__(self):
		return self.guest_name


	
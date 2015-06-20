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
		my_name = my_name[0:len(my_name) - 2]
		return my_name

	def __str__(self):
		return self.pretty_rsvp_name()



class Guest(models.Model):
	rsvp_response = models.ForeignKey(RsvpResponse)
	guest_name = models.CharField(max_length=200)
	attending_choices = ((None, 'No response'), (False, 'Not Attending'), (True, "Attending"))
	guest_attending = models.NullBooleanField(choices=attending_choices)
	drink_choices = ((None, 'No alcohol'),(True, 'Beer'),(False,'Wine'))
	guest_drink_pref = models.NullBooleanField(choices=drink_choices)

	def __str__(self):
		return self.guest_name


	
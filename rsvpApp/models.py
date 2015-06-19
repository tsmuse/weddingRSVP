import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class RsvpResponse(models.Model):
	response_date = models.DateTimeField('responded on')

	""" 
	what I want to do here is derrive the name of the RSVP from all the child guest_name values
	but I can't figure out if it's possible or not. Can prettify in views, so this is a placeholder.
	"""
	def __str__(self):
		return "RSVP " + str(self.id)


class Guest(models.Model):
	rsvp_response = models.ForeignKey(RsvpResponse)
	guest_name = models.CharField(max_length=200)
	guest_attending = models.NullBooleanField()
	# to get a rough count of beer drinkers vs wine drinkers
	# True == Beer False == Wine
	guest_drink_pref = models.BooleanField()
	def __str__(self):
		return self.guest_name


	
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class RsvpResponse(models.Model):
	response_date = models.DateTimeField('responded on')
	

class Guest(models.Model):
	rsvp_response = models.ForeignKey(RsvpResponse)
	guest_name = models.CharField(max_length=200)
	guest_attending = models.NullBooleanField()
	# to get a rough count of beer drinkers vs wine drinkers
	# True == Beer False == Wine
	guest_drink_pref = models.BooleanField()
	def __str__(self):
		return self.guest_name


	
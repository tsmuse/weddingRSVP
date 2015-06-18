from django.shortcuts import render

# Create your views here.

""" 
Saving for later. Retreiving a specific RSVP: rsvp = RsvpResponse.objects.get(guest__guest_name__iexact=GUESTNAME)
This returns the RsvpResponse object that contains all the guests on that Rsvp 
"""


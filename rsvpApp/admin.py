from django.contrib import admin

# Register your models here.
from .models import RsvpResponse, Guest


class GuestInLine(admin.TabularInline):
	model = Guest
	extra = 0
	fields = ('guest_name','guest_attending', 'guest_drink_pref')


def rsvp_attenting(obj):
	attending = "Not Attending"
	for guest in obj.guest_set.all():
		if guest.guest_attending == True:
			attending = "Attending"
	return attending


class RsvpResponseAdmin(admin.ModelAdmin):
	inlines = [GuestInLine]
	list_display = ("pretty_rsvp_name", rsvp_attenting, "response_date")
	




admin.site.register(RsvpResponse, RsvpResponseAdmin)
from django.contrib import admin

# Register your models here.
from .models import RsvpResponse, Guest


class GuestInLine(admin.TabularInline):
	model = Guest
	extra = 0
	fields = ('guest_name','guest_attending', 'guest_drink_pref')


def rsvp_attending(obj):
	"""
	the user facing response form will not allow None values to be submitted
	so the only time any guest_attending will == None is when they all do
	"""
	attending = "Not Attending"
	guest_list = obj.guest_set.filter(guest_attending=None)
	if len(guest_list) > 0:
		attending = "No response"
	guest_list = obj.guest_set.filter(guest_attending=True)
	if len(guest_list) > 0:
		attending = "Attending"
	return attending


class RsvpResponseAdmin(admin.ModelAdmin):
	inlines = [GuestInLine]
	list_display = ("pretty_rsvp_name", rsvp_attending, "response_date")
	




admin.site.register(RsvpResponse, RsvpResponseAdmin)
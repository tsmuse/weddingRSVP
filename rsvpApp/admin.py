from django.contrib import admin

# Register your models here.
from .models import RsvpResponse, Guest

class GuestInLine(admin.TabularInline):
	model = Guest
	extra = 0
	list_display = ('guest_name','guest_attending', 'guest_drink_pref')

def pretty_rsvp_name(obj):
	my_name = "RSVP for "
	for guest in obj.guest_set.all():
		my_name += guest.guest_name + ", "	
	return my_name


class RsvpResponseAdmin(admin.ModelAdmin):
	inlines = [GuestInLine]
	list_display = (pretty_rsvp_name,)
	




admin.site.register(RsvpResponse, RsvpResponseAdmin)
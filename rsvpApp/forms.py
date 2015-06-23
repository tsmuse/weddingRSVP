from django import forms
from django.forms.extras import widgets
from rsvpApp.models import RsvpResponse, Guest


class IndexSearchForm(forms.Form):
	search_field = forms.CharField(label="Enter one name from your address label", max_length=200)

class RsvpForm(forms.ModelForm):
	attending_choices = ((False, 'Not Attending'), (True, "Attending"))
	guest_attending = forms.NullBooleanField(widget=widgets.Select(choices=attending_choices ))
	class Meta:
		model = Guest
		fields = ('guest_attending', 'guest_drink_pref')



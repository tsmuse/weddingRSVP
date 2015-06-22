from django import forms
from rsvpApp.models import RsvpResponse, Guest


class IndexSearchForm(forms.Form):
	search_field = forms.CharField(label="Enter one name from your address label", max_length=200)

class RsvpForm(forms.ModelForm):
	class Meta:
		model = Guest
		fields = ('guest_attending', 'guest_drink_pref')
		



from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.forms import widgets
from django.forms.models import inlineformset_factory
from django.views import generic
from django.utils import timezone

from .models import RsvpResponse, Guest 
from . import forms


class IndexView(generic.FormView):
	template_name = "index.html"
	form_class = forms.IndexSearchForm

def search_result(request):
	name = request.GET.get('search_field', '')
	try:
		rsvp = RsvpResponse.objects.get(guest__guest_name__iexact=name)
	except:
		return render(request, 'index.html', {'search': name, 
			'error_message': "Sorry, that name isn't on the list.",
			'form': forms.IndexSearchForm
		})
	else:
		return render(request, 'rsvpfind.html', {'rsvp': rsvp})

def rsvp_respond(request, rsvp_id):
	rsvp = get_object_or_404(RsvpResponse, pk=rsvp_id)
	RsvpInlineFormSet = inlineformset_factory(RsvpResponse, Guest, 
		form=forms.RsvpForm, 
		extra=0
	)
	if request.method == "POST":
		
		formset = RsvpInlineFormSet(request.POST, instance=rsvp)

		if formset.is_valid():
			# save the updated response date. I don't know how to do this yet w/o hitting the db twice
			rsvp.response_date = timezone.now()
			rsvp.save()
			formset.save()
			return HttpResponseRedirect(reverse('rsvpApp:results', args=(rsvp.id,)))
		else:
			return render(request, 'respond.html', {'formset': formset, 'rsvpresponse': rsvp, 'error_message': formset.errors,})

	else:
		"""
		holy shit, it took me 3 hours to figure out this cool fix to my problem of being able to call items in
		the guest_set of the rsvp object along side their InlineFormSet counterparts. zip FTW!
		"""
		formset = RsvpInlineFormSet(instance=rsvp)
		guests = rsvp.guest_set.all()
		formset_and_guests = zip(formset,guests)
		return render(request, 'respond.html', {'formset': formset, 'rsvpresponse': rsvp, 'formset_and_guests': formset_and_guests})


class ResultsView(generic.DetailView):
	model = RsvpResponse
	template_name = "results.html"


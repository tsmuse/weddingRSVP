from django.test import TestCase

import datetime

from django.utils import timezone
from django.test import TestCase

from .models import RsvpResponse, Guest

def create_rsvp(guest_count, days):
	"""
	Creates an RsvpResponse with the specified number of guests
	and a response date that is days offset from timezone.now()
	"""
	rsvp = RsvpResponse(response_date=(timezone.now() + datetime.timedelta(days)))
	rsvp.save()

	if guest_count == 1:
		# if there is only 1 guest, that person gets a +1
		rsvp.guest_set.create(guest_name="Test Guest 1", guest_attending=None, guest_drink_pref=False)
		rsvp.guest_set.create(guest_name="Test Guest 1 guest", guest_attending=None, guest_drink_pref=False)
	else:
		# there is no +1, only the invited guests
		for n in range(1, guest_count + 1):
			rsvp.guest_set.create(guest_name='Test guest ' + str(n), guest_attending=None, guest_drink_pref=False)
	return rsvp

class HelperFunctionTests(TestCase):
	def test_create_rsvp_single_guest(self):
		"""
		Since I'm new to all of this Python stuff I'm creating some tests that are
		probably way too fine-grained. Checking my create_rsvp helper to make sure
		it returns one guest with a + 1 when guest_count == 1
		"""
		test_rsvp = create_rsvp(1, 5)
		plus_one = test_rsvp.guest_set.get(guest_name__exact='Test Guest 1 guest')
		self.assertEqual(len(test_rsvp.guest_set.all()) == 2, True)
		self.assertEqual(plus_one.guest_name == 'Test Guest 1 guest', True)

	def test_create_rsvp_five_guests(self):
		"""
		Since I'm new to all of this Python stuff I'm creating some tests that are
		probably way too fine-grained. Checking my create_rsvp helper to make sure
		it returns 5 guests with no + 1 when guest_count == 5
		"""
		test_rsvp = create_rsvp(5, 10)
		is_plus_one = False
		if test_rsvp.guest_set.filter(guest_name__contains='Test Guest 1 guest').count() > 0:
			is_plus_one = True

		self.assertEqual(len(test_rsvp.guest_set.all()) == 5, True)
		self.assertEqual(is_plus_one, False)

class RsvpResponseModelTests(TestCase):
	def test_pretty_rsvp_name(self):
		"""
		Test that the pretty name will always be the combined
		names of all the guests in the rsvp
		"""
		pretty_name = "RSVP for Test guest 1, Test guest 2"
		rsvp = create_rsvp(2, 10)
		self.assertEqual(rsvp.pretty_rsvp_name() == pretty_name, True)
		


# Create your tests here.
# You're not the boss of me, auto-generated comment line
from django.test import SimpleTestCase, TestCase
from django.contrib.auth import get_user_model
from django.urls import	reverse

from main_app.forms import RegisterUserForm

class RegistrationFormTests(TestCase):	
	def test_registration_form(self):
		response = self.client.post(
			reverse("registration"),
			{
				"username": "name",
				"email": "name@example.com",
				"password1": "testpass123",
				"password2": "testpass123",
			},
		)
		self.assertEqual(response.status_code, 302)
		self.assertEqual(get_user_model().objects.all().count(), 1)
		self.assertEqual(get_user_model().objects.all()[0].username, "name")
		self.assertEqual(get_user_model().objects.all()[0].email, "name@example.com")
		

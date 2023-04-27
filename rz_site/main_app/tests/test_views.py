from django.test import TestCase
from django.urls import	reverse


class IndexViewTests(TestCase):
	def test_url_exists_at_correct_location(self):
		response = self.client.get("/")
		self.assertEqual(response.status_code, 200)
	
	def test_page(self):
		response = self.client.get(reverse("index"))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, "main_app/index.html")
		#self.assertContains(response, "<title>Главная страница</title>")
		
		
class WorkExamplesViewTests(TestCase):
	def test_url_exists_at_correct_location(self):
		response = self.client.get("/work_examples/")
		self.assertEqual(response.status_code, 200)
		
	def test_page(self):
		response = self.client.get(reverse("work_examples"))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, "main_app/work_examples.html")
		

class ReviewsViewTests(TestCase):
	def test_url_exists_at_correct_location(self):
		response = self.client.get("/reviews/")
		self.assertEqual(response.status_code, 200)
		
	def test_page(self):
		response = self.client.get(reverse("reviews"))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, "main_app/reviews.html")


class ArticlesViewTests(TestCase):
	def test_url_exists_at_correct_location(self):
		response = self.client.get("/articles/")
		self.assertEqual(response.status_code, 200)
		
	def test_page(self):
		response = self.client.get(reverse("articles"))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, "main_app/articles.html")
		
		
class RegistrationViewTests(TestCase):
	def test_url_exists_at_correct_location(self):
		response = self.client.get("/registration/")
		self.assertEqual(response.status_code, 200)
		
	def test_page_view(self):
		response = self.client.get(reverse("registration"))
		self.assertEqual(response.status_code, 200)
		#self.assertTemplateUsed(response, "registration.html")
		

class LogoutViewTests(TestCase):
	def test_url_exists_at_correct_location(self):
		response = self.client.get("/logout/")
		self.assertEqual(response.status_code, 200)
		
	def test_page(self):
		response = self.client.get(reverse("logout"))
		self.assertEqual(response.status_code, 200)
		#self.assertTemplateUsed(response, "main_app/logout.html")
		

class AuthorizationViewTests(TestCase):
	def test_url_exists_at_correct_location(self):
		response = self.client.get("/authorization/")
		self.assertEqual(response.status_code, 200)
		
	def test_page(self):
		response = self.client.get(reverse("authorization"))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, "main_app/authorization.html")

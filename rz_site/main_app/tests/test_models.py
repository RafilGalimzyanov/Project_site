from django.test import SimpleTestCase, TestCase

from main_app.models import Article, Review

class ArticleModelTests(TestCase):
	@classmethod
	def setUpClass(cls):
		super().setUpClass()
		cls.article = Article.objects.create(
			title="title example",
			content="content example",
		)
	
	def test_model_content(self):
		self.assertEqual(self.article.title, "title example")
		self.assertEqual(self.article.content, "content example")
		self.assertEqual(str(self.article), "title example")


class ReviewModelTests(TestCase):
	@classmethod
	def setUpClass(cls):
		super().setUpClass()
		cls.review = Review.objects.create(
			email="username@example.com",
			name="username",
			rev = "review example",
		)
	
	def test_model_content(self):
		self.assertEqual(self.review.email, "username@example.com")
		self.assertEqual(self.review.name, "username")
		self.assertEqual(self.review.rev, "review example")
		self.assertEqual(str(self.review), "username")

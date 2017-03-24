from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.staticfiles import finders

class GeneralTests(TestCase):
    def test_serving_static_files(self):
        # If using static media properly result is not NONE once it finds rango.jpg
        result = finders.find('images/lachesis.jpg')
        self.assertIsNotNone(result)


class IndexPageTests(TestCase):
    def test_index_using_template(self):
        # Check the template used to render index page
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'lachesis/index.html')

    def test_index_has_title(self):
        # Check to make sure that the title tag has been used
        response = self.client.get(reverse('index'))
        self.assertIn(b'<title>', response.content)
        self.assertIn(b'</title>', response.content)
		
	def test_about_contains_home_button(self):
        # Check if in the about page is there - and contains the specified message
        response = self.client.get(reverse('index'))
        self.assertIn(b'home', response.content)
		
	def test_about_contains_about_button(self):
        # Check if in the about page is there - and contains the specified message
        response = self.client.get(reverse('about'))
        self.assertIn(b'about', response.content)


class AboutPageTests(TestCase):
    def test_about_contains_create_message(self):
        # Check if in the about page is there - and contains the specified message
        response = self.client.get(reverse('about'))
        self.assertIn(b'The purpose of our', response.content)

    def test_about_contain_image(self):
        # Check if is there an image on the about page
        response = self.client.get(reverse('about'))
        self.assertIn(b'img src="/images/', response.content)

    def test_about_using_template(self):
        # Check the template used to render index page
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'lachesis/about.html')

class ViewTests(TestCase):
    def test_does_index_contain_img(self):
        # Check if the index page contains an img
        response = self.client.get(reverse('index'))
        self.assertIn('img', response.content)

    def test_about_using_template(self):
        # Check the template used to render index page
        # Exercise from Chapter 4
        response = self.client.get(reverse('about'))

        self.assertTemplateUsed(response, 'lachesis/about.html')

    def test_does_about_contain_img(self):
        # Check if in the about page contains an image
        response = self.client.get(reverse('about'))
        self.assertIn('img', response.content)
		
class SlugTests(TestCase):

    # test the slug field works..
    def test_does_slug_field_work(self):
        from lachesis.models import Genre
        gen = Genre(name='how do i create a slug in django')
        gen.save()
        self.assertEqual(gen.slug, 'how-do-i-create-a-slug-in-django')

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.staticfiles import finders

class GeneralTests(TestCase):
    def test_serving_static_files(self):
        result = finders.find('images/lachesis.jpg')
        self.assertIsNotNone(result)


class IndexPageTests(TestCase):
    def test_index_contains_hello_message(self):
        response = self.client.get(reverse('index'))
        self.assertIn(b'lachesis says', response.content)

    def test_index_using_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'lachesis/index.html')

    def test_lachesis_picture_displayed(self):
        response = self.client.get(reverse('index'))
        self.assertIn(b'img src="/static/images/lachesis.jpg', response.content)

    def test_index_has_title(self):
        response = self.client.get(reverse('index'))
        self.assertIn(b'<title>', response.content)
        self.assertIn(b'</title>', response.content)


class AboutPageTests(TestCase):
    def test_about_contains_create_message(self):
        response = self.client.get(reverse('about'))
        self.assertIn(b'This tutorial has been put together by', response.content)

    def test_about_contain_image(self):
        response = self.client.get(reverse('about'))
        self.assertIn(b'img src="/media/', response.content)

    def test_about_using_template(self):
        response = self.client.get(reverse('about'))

        self.assertTemplateUsed(response, 'lachesis/about.html')


class ModelTests(TestCase):
    def setUp(self):
        try:
            from populate_lachesis import populate
            populate()
        except ImportError:
            print('The module populate_lachesis does not exist')
        except NameError:
            print('The function populate() does not exist or is not correct')
        except:
            print('Something went wrong in the populate() function :-(')

    def get_category(self, name):

        from lachesis.models import Category
        try:
            cat = Category.objects.get(name=name)
        except Category.DoesNotExist:
            cat = None
        return cat

    def test_python_cat_added(self):
        cat = self.get_category('Python')
        self.assertIsNotNone(cat)

    def test_python_cat_with_views(self):
        cat = self.get_category('Python')
        self.assertEquals(cat.views, 128)

    def test_python_cat_with_likes(self):
        cat = self.get_category('Python')
        self.assertEquals(cat.likes, 64)


class Chapter4ViewTests(TestCase):
    def test_index_contains_hello_message(self):
        response = self.client.get(reverse('index'))
        self.assertIn('lachesis says', response.content)

    def test_does_index_contain_img(self):
        response = self.client.get(reverse('index'))
        self.assertIn('img', response.content)

    def test_about_using_template(self):
        response = self.client.get(reverse('about'))

        self.assertTemplateUsed(response, 'lachesis/about.html')

    def test_does_about_contain_img(self):
        response = self.client.get(reverse('about'))
        self.assertIn('img', response.content)

    def test_about_contains_create_message(self):
        response = self.client.get(reverse('about'))
        self.assertIn('This tutorial has been put together by', response.content)


class Chapter5ViewTests(TestCase):
    def setUp(self):
        try:
            from populate_lachesis import populate
            populate()
        except ImportError:
            print('The module populate_lachesis does not exist')
        except NameError:
            print('The function populate() does not exist or is not correct')
        except:
            print('Something went wrong in the populate() function :-(')

    def get_category(self, name):

        from lachesis.models import Category
        try:
            cat = Category.objects.get(name=name)
        except Category.DoesNotExist:
            cat = None
        return cat

    def test_python_cat_added(self):
        cat = self.get_category('Python')
        self.assertIsNotNone(cat)

    def test_python_cat_with_views(self):
        cat = self.get_category('Python')

        self.assertEquals(cat.views, 128)

    def test_python_cat_with_likes(self):
        cat = self.get_category('Python')
        self.assertEquals(cat.likes, 64)

    def test_view_has_title(self):
        response = self.client.get(reverse('index'))

        self.assertIn('<title>', response.content)
        self.assertIn('</title>', response.content)

    def test_admin_interface_page_view(self):
        from admin import PageAdmin
        self.assertIn('category', PageAdmin.list_display)
        self.assertIn('url', PageAdmin.list_display)


class Chapter6ViewTests(TestCase):
    def setUp(self):
        try:
            from populate_lachesis import populate
            populate()
        except ImportError:
            print('The module populate_lachesis does not exist')
        except NameError:
            print('The function populate() does not exist or is not correct')
        except:
            print('Something went wrong in the populate() function :-(')

    def test_does_slug_field_work(self):
        from lachesis.models import Category
        cat = Category(name='how do i create a slug in django')
        cat.save()
        self.assertEqual(cat.slug, 'how-do-i-create-a-slug-in-django')

class Chapter7ViewTests(TestCase):
    def setUp(self):
        try:
            from forms import PageForm
            from forms import CategoryForm

        except ImportError:
            print('The module forms does not exist')
        except NameError:
            print('The class PageForm does not exist or is not correct')
        except:
            print('Something else went wrong :-(')

    pass

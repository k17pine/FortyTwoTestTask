from django.test import TestCase, SimpleTestCase


class SomeTests(TestCase):
    def test_math(self):
        "put docstrings in your tests"
        assert(2 + 2 == 4)


class HomePageTests(SimpleTestCase):

    def test_home_page_status_code(self):
    	"put docstrings in your tests"
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

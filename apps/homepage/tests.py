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

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<h3>42 Coffee Cups Test Assignment</h')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(response, 'Hi! I should not be on the page.')

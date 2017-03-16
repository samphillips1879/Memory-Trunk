from django.test import TestCase, Client
from django.urls import reverse

from django.contrib.auth.models import User

class TestIndexView(TestCase):
    """
    Purpose:
        Tests the rendering of the home page

    Methods:
        test_index_view_is_rendered_properly

    Author: Sam Phillips <samcphillips.com>
    """
    def test_index_view_is_rendered_properly(self):
        response = self.client.get(reverse('memory_trunk_app:index'))
        self.assertTemplateUsed('index.html')
        self.assertEqual(response.status_code, 200)
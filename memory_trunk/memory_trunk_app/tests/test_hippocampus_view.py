from django.test import TestCase, Client
from django.urls import reverse

from django.contrib.auth.models import User

class TestHippocampusView(TestCase):
    """
    Purpose:
        Tests the rendering of the memory creation form view

    Methods:
        test_hippocampus_is_rendered_properly

    Author: Sam Phillips <samcphillips.com>
    """
    def test_hippocampus_redirects_unauthenticated_users(self):
        response = self.client.get(reverse('memory_trunk_app:hippocampus'))
        self.assertTemplateUsed('hippocampus.html')
        self.assertEqual(response.status_code, 302)
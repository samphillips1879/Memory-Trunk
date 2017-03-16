from django.test import TestCase, Client
from django.urls import reverse

from django.contrib.auth.models import User

class TestLogoutUser(TestCase):
    """
    Purpose:
        Tests the functionality of logging out a user

    Methods:
        test_logout_redirects_to_index

    Author: Sam Phillips <samcphillips.com>
    """
    def test_logout_redirects_to_index(self):
        response = self.client.get(reverse('memory_trunk_app:logout_user'))
        self.assertRedirects(response, '/')
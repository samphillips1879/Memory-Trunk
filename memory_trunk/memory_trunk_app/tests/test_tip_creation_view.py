from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class TestTipCreationView(TestCase):
    """
    Purpose:
        Tests the processing of the Tip creation view

    Methods:
        test_tip_creation_redirects_unauthenticated_users

    Author: Sam Phillips <samcphillips.com>
    """
    def test_tip_creation_redirects_unauthenticated_users(self):
        response = self.client.get(reverse('memory_trunk_app:tip_creation'))
        self.assertTemplateUsed('tip_creation.html')
        self.assertEqual(response.status_code, 302)
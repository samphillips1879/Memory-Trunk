from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class TestPerspectiveCreationView(TestCase):
    """
    Purpose:
        Tests the processing of the Perspective creation view

    Methods:
        test_perspective_creation_redirects_unauthenticated_users

    Author: Sam Phillips <samcphillips.com>
    """
    def test_perspective_creation_redirects_unauthenticated_users(self):
        response = self.client.get(reverse('memory_trunk_app:perspective_creation'))
        self.assertTemplateUsed('perspective_creation.html')
        self.assertEqual(response.status_code, 302)
from django.test import TestCase, Client
from django.urls import reverse

from django.contrib.auth.models import User

class TestRegisterUserView(TestCase):
    """
    Purpose:
        Tests the rendering of the user registration form

    Methods:
        test_registration_form_is_rendered_properly

    Author: Sam Phillips <samcphillips.com>
    """
    def test_registration_form_is_rendered_properly(self):
        response = self.client.get(reverse('memory_trunk_app:user_registration'))
        self.assertTemplateUsed('register.html')
        self.assertEqual(response.status_code, 200)
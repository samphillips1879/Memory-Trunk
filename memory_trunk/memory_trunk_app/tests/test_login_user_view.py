from django.test import TestCase, Client
from django.urls import reverse

from django.contrib.auth.models import User

class TestLoginUserView(TestCase):
    """
    Purpose:
        Tests the rendering of the user login form

    Methods:
        test_login_form_is_rendered_properly

    Author: Sam Phillips <samcphillips.com>
    """
    def test_login_form_is_rendered_properly(self):
        response = self.client.get(reverse('memory_trunk_app:login_user_view'))
        self.assertTemplateUsed('login_user.html')
        self.assertEqual(response.status_code, 200)
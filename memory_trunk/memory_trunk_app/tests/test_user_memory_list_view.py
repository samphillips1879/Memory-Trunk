from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class TestHippocampusView(TestCase):
    """
    Purpose:
        Tests the processing of the user-specific memory list view

    Methods:
        test_memory_list_view_redirects_unauthenticated_users

    Author: Sam Phillips <samcphillips.com>
    """
    def test_memory_list_view_redirects_unauthenticated_users(self):
        response = self.client.get(reverse('memory_trunk_app:memory_list', args=(1,)))
        self.assertTemplateUsed('memory_list.html')
        self.assertEqual(response.status_code, 302)
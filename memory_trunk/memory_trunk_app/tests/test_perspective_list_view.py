from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class TestPerspectiveListView(TestCase):
    """
    Purpose:
        Tests the processing of the user-specific Perspective list view

    Methods:
        test_perspective_list_view_redirects_unauthenticated_users

    Author: Sam Phillips <samcphillips.com>
    """
    def test_perspective_list_view_redirects_unauthenticated_users(self):
        response = self.client.get(reverse('memory_trunk_app:perspective_list', args=(1,)))
        self.assertTemplateUsed('perspective_list.html')
        self.assertEqual(response.status_code, 302)

    def test_public_perspective_list_view_renders_properly(self):
        response = self.client.get(reverse('memory_trunk_app:public_perspective_list'))
        self.assertContains(response, 'Community Perspectives')
        self.assertEqual(response.status_code, 200)
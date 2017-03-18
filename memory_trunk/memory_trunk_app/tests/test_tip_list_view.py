from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class TestTipListView(TestCase):
    """
    Purpose:
        Tests the processing of the user-specific Tip list view

    Methods:
        test_tip_list_view_redirects_unauthenticated_users

    Author: Sam Phillips <samcphillips.com>
    """
    def test_tip_list_view_redirects_unauthenticated_users(self):
        response = self.client.get(reverse('memory_trunk_app:tip_list', args=(1,)))
        self.assertTemplateUsed('tip_list.html')
        self.assertEqual(response.status_code, 302)

    def test_public_tip_list_view_renders_properly(self):
        response = self.client.get(reverse('memory_trunk_app:public_tip_list'))
        self.assertContains(response, 'Community Tips')
        self.assertEqual(response.status_code, 200)
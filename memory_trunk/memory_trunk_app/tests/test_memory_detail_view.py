from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class TestMemoryDetailView(TestCase):
    """
    Purpose:
        Tests the processing of the Memory detail view

    Methods:
        test_memory_detail_view_renders_properly
        test_private_memories_are_not_visible_to_the_public

    Author: Sam Phillips <samcphillips.com>
    """
    # def test_memory_list_view_redirects_unauthenticated_users(self):
    #     response = self.client.get(reverse('memory_trunk_app:memory_list', args=(1,)))
    #     self.assertTemplateUsed('memory_list.html')
    #     self.assertEqual(response.status_code, 302)

    def test_memory_detail_view_renders_properly(self):
        self.assertTrue(False)

    def test_private_memories_are_not_visible_to_the_public(self):
        self.assertTrue(False)

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from memory_trunk_app import models
import datetime

class TestMemoryDetailView(TestCase):
    """
    Purpose:
        Tests the processing of the Memory detail view

    Methods:
        setUpTestData
        test_memory_detail_view_renders_properly
        test_private_memories_are_not_visible_to_the_public

    Author: Sam Phillips <samcphillips.com>
    """
    def test_memory_list_view_redirects_unauthenticated_users(self):
        response = self.client.get(reverse('memory_trunk_app:memory_list', args=(1,)))
        self.assertTemplateUsed('memory_list.html')
        self.assertEqual(response.status_code, 302)

    @classmethod
    def setUpTestData(self):
        self.user = User.objects.create(
            first_name = "Mark",
            last_name = "Twain",
            email = "mark@twain.com",
            username = "MarkTwain",
            password="Pass1234"
        )

        self.new_memory = models.Memory.objects.create(
            user = self.user,
            title = "Theodore's Birth",
            is_public = 1,
            date = datetime.date.today(),
            location = "Williamson Medical Center",
            content = "Theodore was born and it was amazing!",
            happy_factor = 10,
            sad_factor = 0
        )

        self.private_memory = models.Memory.objects.create(
            user = self.user,
            title = "Theodore's Secret Birth",
            is_public = 0,
            date = datetime.date.today(),
            location = "Williamson Medical Center",
            content = "Theodore was born and it was amazing!",
            happy_factor = 10,
            sad_factor = 0
        )

        self.all_memories = models.Memory.objects.all()

    def test_memory_detail_view_renders_properly(self):
        response = self.client.get(reverse('memory_trunk_app:memory_detail', args=(len(self.all_memories) - 1,)))
        self.assertContains(response, "Williamson Medical Center")
        self.assertEqual(response.status_code, 200)

    def test_private_memories_are_not_visible_to_the_public(self):
        response = self.client.get(reverse('memory_trunk_app:memory_detail', args=(len(self.all_memories),)))
        self.assertTemplateUsed('memory_detail.html')
        self.assertEqual(response.status_code, 302)
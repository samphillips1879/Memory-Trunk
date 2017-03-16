from django.test import TestCase
from django.contrib.auth.models import User
from memory_trunk_app import models
import datetime

class TestMemoryModel(TestCase):
    """
    Purpose:
        Tests the instantiation of the Memory model

    Methods:
        setUpTestData
        test_new_memory_is_of_class_Memory
        test_new_memory_properties_are_initialized_properly
        test_memories_can_be_tagged
        test_memories_can_be_liked_by_users

    Author: Sam Phillips <samcphillips.com>
    """

    @classmethod
    def setUpTestData(self):
        self.user = User.objects.create(
            first_name = "Mark",
            last_name = "Twain",
            email = "mark@twain.com",
            username = "MarkTwain",
            password="Pass1234"
        )

        self.user_1 = User.objects.create(
            first_name = "Danny",
            last_name = "Devito",
            email = "danny@devito.com",
            username = "DannyDevito",
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

        self.tags = ["Theodore", "Birth", "Parenthood"]

    def test_new_memory_is_of_class_Memory(self):
        self.assertIsInstance(self.new_memory, models.Memory)

    def test_new_memory_properties_are_initialized_properly(self):
        self.assertEqual(self.user, self.new_memory.user)
        self.assertEqual(self.new_memory.title, "Theodore's Birth")
        self.assertEqual(self.new_memory.is_public, 1)
        self.assertIsInstance(self.new_memory.date, datetime.date)
        self.assertEqual(
            self.new_memory.location, 
            "Williamson Medical Center"
        )
        self.assertEqual(
            self.new_memory.content, 
            "Theodore was born and it was amazing!"
        )
        self.assertEqual(self.new_memory.happy_factor, 10)
        self.assertEqual(self.new_memory.sad_factor, 0)
        self.assertIsNotNone(self.new_memory.tags)
        self.assertIsNotNone(self.new_memory.likes)

    def test_memories_can_be_tagged(self):
        for tag in self.tags:
            self.assertNotIn(tag, self.new_memory.tags.names())
        self.new_memory.add_tags(self.tags)
        for tag in self.tags:
            self.assertIn(tag, self.new_memory.tags.names())

    def test_memories_can_be_liked_by_users(self):
        self.assertNotIn(self.user_1, self.new_memory.likes.all())
        self.new_memory.add_like(self.user_1)
        self.assertIn(self.user_1, self.new_memory.likes.all())

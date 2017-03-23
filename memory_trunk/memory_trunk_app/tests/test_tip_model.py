from django.test import TestCase
from django.contrib.auth.models import User
from memory_trunk_app import models
import datetime

class TestTipModel(TestCase):
    """
    Purpose:
        Tests the instantiation and all methods of the Tip model

    Methods:
        setUpTestData
        test_new_tip_is_of_class_Tip
        test_new_tip_values_are_instantiated_properly
        test_tip_can_be_tagged_with_keywords
        test_tip_can_be_related_to_a_memory
        test_tip_can_be_liked_by_users

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

        self.tags = ["Birth", "Parenthood", "Sleep",]

        self.new_tip = models.Tip.objects.create(
            user = self.user,
            title = "Sleep as much as you can before having a baby",
            is_public = 1,
            content = """
                Having a baby is amazing, but it's also exhausting. 
                Everybody tells you that you won't be able to get any sleep
                afterwards, but I hadn't realized just how tiresome it could 
                be. If I were to do it again, I'd definitely have made a 
                point to sleep better the week before his due date.
            """
        )

    def test_new_tip_is_of_class_Tip(self):
        self.assertIsInstance(self.new_tip, models.Tip)

    def test_new_tip_values_are_instantiated_properly(self):
        self.assertEqual(self.user, self.new_tip.user)
        self.assertEqual(
            "Sleep as much as you can before having a baby", 
            self.new_tip.title
        )
        self.assertEqual(1, self.new_tip.is_public)
        self.assertEqual("""
                Having a baby is amazing, but it's also exhausting. 
                Everybody tells you that you won't be able to get any sleep
                afterwards, but I hadn't realized just how tiresome it could 
                be. If I were to do it again, I'd definitely have made a 
                point to sleep better the week before his due date.
            """, 
            self.new_tip.content
        )
        self.assertIsNotNone(self.new_tip.tags)
        self.assertIsNotNone(self.new_tip.memories)
        self.assertIsNotNone(self.new_tip.likes)

    def test_tip_can_be_tagged_with_keywords(self):
        for tag in self.tags:
            self.assertNotIn(tag, self.new_tip.tags.names())
        self.new_tip.add_tags(self.tags)
        for tag in self.tags:
            self.assertIn(tag, self.new_tip.tags.names())

    def test_tip_can_be_related_to_a_memory(self):
        self.assertNotIn(self.new_memory, self.new_tip.memories.all())
        self.new_tip.connect_to_memory(self.new_memory)
        self.assertIn(self.new_memory, self.new_tip.memories.all())

    def test_tip_can_be_liked_by_users(self):
        self.assertNotIn(self.user_1, self.new_tip.likes.all())
        self.new_tip.add_like(self.user_1)
        self.assertIn(self.user_1, self.new_tip.likes.all())
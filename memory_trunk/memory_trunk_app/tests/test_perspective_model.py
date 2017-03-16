from django.test import TestCase
from django.contrib.auth.models import User
from memory_trunk_app import models
import datetime

class TestPerspectiveModel(TestCase):
    """
    Purpose:
        Tests the instantiation and all methods of the Perspective model

    Methods:
        setUpTestData
        test_new_perspective_is_of_class_Perspective
        test_new_perspective_values_are_instantiated_properly
        test_perspective_can_be_tagged_with_keywords
        test_perspective_can_be_related_to_a_memory
        test_perspective_can_be_liked_by_users

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

        self.new_perspective = models.Perspective.objects.create(
            user = self.user,
            title = "Hakuna Matata",
            is_public = 1,
            content = """
            There are countless reasons to be stressed out in life, but most 
            of the time letting yourself get stressed out only makes things 
            worse. I find that I'm a lot happier when I embrace a Hakuna 
            Matata (no worries) attitude. That doesn't mean ignoring your 
            problems and responsibilities, it just means remembering that
            you can tackle them better with a cool head and a light heart.
            Crying babies are soothed easier by calm parents, interpersonal 
            conflicts are solved more quickly without personal feelings 
            getting in the way, and anxiety dissapears in the face of 
            letting go.
            """
        )

    def test_new_perspective_is_of_class_Perspective(self):
        self.assertIsInstance(self.new_perspective, models.Perspective)

    def test_new_perspective_values_are_instantiated_properly(self):
        self.assertEqual(self.user, self.new_perspective.user)
        self.assertEqual("Hakuna Matata", self.new_perspective.title)
        self.assertEqual(1, self.new_perspective.is_public)
        self.assertEqual("""
            There are countless reasons to be stressed out in life, but most 
            of the time letting yourself get stressed out only makes things 
            worse. I find that I'm a lot happier when I embrace a Hakuna 
            Matata (no worries) attitude. That doesn't mean ignoring your 
            problems and responsibilities, it just means remembering that
            you can tackle them better with a cool head and a light heart.
            Crying babies are soothed easier by calm parents, interpersonal 
            conflicts are solved more quickly without personal feelings 
            getting in the way, and anxiety dissapears in the face of 
            letting go.
            """, 
            self.new_perspective.content
        )
        self.assertIsNotNone(self.new_perspective.likes)
        self.assertIsNotNone(self.new_perspective.memories)
        self.assertIsNotNone(self.new_perspective.tags)

    def test_perspective_can_be_tagged_with_keywords(self):
        for tag in self.tags:
            self.assertNotIn(tag, self.new_perspective.tags.names())
        self.new_perspective.add_tags(self.tags)
        for tag in self.tags:
            self.assertIn(tag, self.new_perspective.tags.names())

    def test_perspective_can_be_related_to_a_memory(self):
        self.assertNotIn(
            self.new_memory, 
            self.new_perspective.memories.all()
        )
        self.new_perspective.connect_to_memory(self.new_memory)
        self.assertIn(self.new_memory, self.new_perspective.memories.all())

    def test_perspective_can_be_liked_by_users(self):
        self.assertNotIn(self.user_1, self.new_perspective.likes.all())
        self.new_perspective.add_like(self.user_1)
        self.assertIn(self.user_1, self.new_perspective.likes.all())
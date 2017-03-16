from django.test import TestCase
from django.contrib.auth.models import User
from memory_trunk_app import models
from memory_trunk_app.models.profile_model import Profile

class TestProfileModel(TestCase):
    """
    Purpose: 
        Tests the instantiation of the Profile model and all methods
        attached to it

    Methods:
        setUpTestData
        test_new_profile_is_of_class_Profile
        test_new_profile_values_are_instantiated
        test_users_can_be_followed
        test_users_can_be_unfollowed

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

    def test_new_profile_is_of_class_Profile(self):
        new_profile = models.Profile.objects.create(user=self.user)
        self.assertIsInstance(new_profile, Profile)

    def test_new_profile_values_are_instantiated(self):
        new_profile = models.Profile.objects.create(user=self.user)
        self.assertEqual(new_profile.user, self.user)
        self.assertIsNotNone(new_profile.users_followed.all())

    def test_users_can_be_followed(self):
        new_profile = models.Profile.objects.create(user=self.user)
        self.assertNotIn(self.user_1, new_profile.users_followed.all())
        new_profile.follow_user(self.user_1)
        self.assertIn(self.user_1, new_profile.users_followed.all())

    def test_users_can_be_unfollowed(self):
        new_profile = models.Profile.objects.create(user=self.user)
        new_profile.follow_user(self.user_1)
        self.assertIn(self.user_1, new_profile.users_followed.all())
        new_profile.unfollow_user(self.user_1)
        self.assertNotIn(self.user_1, new_profile.users_followed.all())
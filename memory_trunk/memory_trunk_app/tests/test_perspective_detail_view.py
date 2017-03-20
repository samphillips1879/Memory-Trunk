from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from memory_trunk_app import models
import datetime

class TestPerspectiveDetailView(TestCase):
    """
    Purpose:
        Tests the processing of the Perspective detail view

    Methods:
        setUpTestData
        test_user_perspective_detail_view_renders_properly
        test_private_perspectives_are_not_visible_to_the_public

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

        self.private_perspective = models.Perspective.objects.create(
            user = self.user,
            title = "Secret Hakuna Matata",
            is_public = 0,
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

        self.all_perspectives = models.Perspective.objects.all()


    def test_perspective_detail_view_renders_properly(self):
        response = self.client.get(reverse('memory_trunk_app:perspective_detail', args=(len(self.all_perspectives) - 1,)))
        self.assertContains(response, "There are countless reasons")
        self.assertEqual(response.status_code, 200)

    def test_private_perspectives_are_not_visible_to_the_public(self):
        response = self.client.get(reverse('memory_trunk_app:perspective_detail', args=(len(self.all_perspectives),)))
        self.assertTemplateUsed('perspective_detail.html')
        self.assertEqual(response.status_code, 302)
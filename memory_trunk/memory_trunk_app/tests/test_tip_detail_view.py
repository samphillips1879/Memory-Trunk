from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from memory_trunk_app import models
import datetime

class TestTipDetailView(TestCase):
    """
    Purpose:
        Tests the processing of the Tip detail view

    Methods:
        setUpTestData
        test_user_tip_detail_view_renders_properly
        test_private_tips_are_not_visible_to_the_public

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

        self.private_tip = models.Tip.objects.create(
            user = self.user,
            title = "Sleep as much as you can before having a baby",
            is_public = 0,
            content = """
                Having a baby is amazing, but it's also exhausting. 
                Everybody tells you that you won't be able to get any sleep
                afterwards, but I hadn't realized just how tiresome it could 
                be. If I were to do it again, I'd definitely have made a 
                point to sleep better the week before his due date.
            """
        )

        self.all_tips = models.Tip.objects.all()


    def test_tip_detail_view_renders_properly(self):
        response = self.client.get(reverse('memory_trunk_app:tip_detail', args=(len(self.all_tips) - 1,)))
        self.assertContains(response, "Having a baby is amazing")
        self.assertEqual(response.status_code, 200)

    def test_private_tips_are_not_visible_to_the_public(self):
        response = self.client.get(reverse('memory_trunk_app:tip_detail', args=(len(self.all_tips),)))
        self.assertTemplateUsed('tip_detail.html')
        self.assertEqual(response.status_code, 302)
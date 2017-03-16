from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """
    Purpose: 
        Used to instantiate new user profiles and maintain their properties

    Properties:
        user -- One to One field connecting a Profile to a django User 
                instance
        users_followed -- Many to Many field representing the other users 
                          followed by this Profile

    Methods:
        follow_user
        unfollow_user

    Author: Sam Phillips <samcphillips.com>
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    users_followed = models.ManyToManyField(User, related_name='profiles')

    def __str__(self):
        """
        Purpose: 
            Create a string representation for the Profile instance
        """
        return "Profile for user: {}".format(self.user)

    def follow_user(self, user):
        """
        Purpose: 
            adds a new User to this Profile's "users_followed" attribute

        Arguments:
            user -- The Django User instance to be followed by this Profile
        """
        self.users_followed.add(user)

    def unfollow_user(self, user):
        """
        Purpose: 
            removes a User from this Profile's "users_followed" attribute

        Arguments:
            user -- The Django User instance this Profile will unfollow
        """
        self.users_followed.remove(user)
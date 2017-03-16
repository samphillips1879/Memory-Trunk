from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Memory(models.Model):
    """
    Purpose:
        Used to create and mantain Memory objects for users

    Properties:
        user -- Django User instance to connect this Memory to the User who 
                created it
        title -- The title of the Memory
        is_public -- Flag to save whether or not this Memory can be viewed 
                     by Users who didn't create it
        date -- When this memory took place
        location -- Where this memory took place
        content -- The main body of a memory, containing the details as a 
                   text string
        happy_factor -- How happy this memory is for the User (integer 0-10)
        sad_factor -- How sad this memory is for the User (integer 0-10)
        tags -- Keywords relating to this Memory 
                (django-taggit https://github.com/alex/django-taggit)
        likes -- Many to Many field tracking which users have "liked" this 
                 Memory

        Methods:
            add_tags
            add_like

        Author: Sam Phillips <samcphillips.com>
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_public = models.PositiveIntegerField()
    date = models.DateField()
    location = models.CharField(max_length=100)
    content = models.TextField()
    happy_factor = models.PositiveIntegerField()
    sad_factor = models.PositiveIntegerField()
    tags = TaggableManager()
    likes = models.ManyToManyField(User, related_name="memory_likes")

    def __str__(self):
        return "{}".format(self.title)

    def add_tags(self, tags):
        """
        Purpose:
            Add tags to this Memory

        Arguments:
            tags -- the keywords to be added to the collection of tags, 
                    can be either a string or a list of strings
        """
        if type(tags) == list:
            for tag in tags:
                self.tags.add(tag)
        elif type(tags) == str:
            self.tags.add(tags)
        else:
            pass

    def add_like(self, user):
        """
        Purpose:
            Provide a way for users to 'like' this Memory

        Arguments:
            user -- The Django User instance that likes this Memory
        """

        self.likes.add(user)




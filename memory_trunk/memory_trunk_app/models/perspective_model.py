from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from memory_trunk_app.models import Memory

class Perspective(models.Model):
    """
    Purpose:
        Used to create and mantain Perspective objects, which are 
        utilized by users to share their perspectives on life or 
        more specific experiences/philosophies

    Properties:
        user -- Django User instance that created this Perspective
        title -- The name of this Perspective/the overarching idea
        is_public -- A flag that determines if users who are not the 
                     creator of this Perspectove are able to view it
        content -- The text body of this Perspective, which expands upon 
                   the title, offering a specific perspective, philosophy, 
                   or way of looking at things
        likes -- Many to Many field tracking which users have "liked" this 
                 Perspective
        memories -- Many To Many field connecting this Perspective to 
                    relevant Memories
        tags -- Keywords relating to this Perspective 
                (django-taggit https://github.com/alex/django-taggit)

    Methods:
        add_like
        add_tags
        connect_to_memory

    Author: Sam Phillips <samcphillips.com>
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, default=True)
    title = models.CharField(max_length=100, default="")
    is_public = models.BooleanField()
    content = models.TextField(default="")
    likes = models.ManyToManyField(User, related_name="perspective_likes")
    memories = models.ManyToManyField(Memory)
    tags = TaggableManager()

    def __str__(self):
        return "{}".format(self.title)

    def add_tags(self, tags):
        """
        Purpose:
            Add tags to this Perspective

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
            Provide a way for users to 'like' this Perspective

        Arguments:
            user -- The Django User instance that likes this Perspective
        """

        self.likes.add(user)

    def connect_to_memory(self, memory):
        """
        Purpose:
            Connect this Perspective to a relevant memory

        Arguments:
            memory -- The Memory instance that this Perspective is related to
        """

        self.memories.add(memory)
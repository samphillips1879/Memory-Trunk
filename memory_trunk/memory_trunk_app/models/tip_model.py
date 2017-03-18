from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from memory_trunk_app.models import Memory

class Tip(models.Model):
    """
    Purpose:
        Used to create and maintain Tip objects, which are utilized by users 
        to offer and organize life advice
    
    Properties:
        user -- Django User instance that created this Tip
        title -- The name of this Tip/the overarching idea
        do -- A flag that determines whether this is a "Do" Tip (1) or a 
              "Do Not" tip (0)
        is_public -- A flag that determines if users who are not the 
                     creator of this Tip are able to view it
        content -- The text body of this Tip, which expands upon the title, 
                   offering specific life advice to users
        tags -- Keywords relating to this Tip 
                (django-taggit https://github.com/alex/django-taggit)
        memories -- Many To Many field connecting this Tip to relevant 
                    Memories
        likes -- Many to Many field tracking which users have "liked" this 
                 Tip

    Methods:
        add_tags
        add_like
        connect_to_memory

    Author: Sam Phillips <samcphillips.com>
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=True)
    title = models.CharField(max_length=100, default="")
    do = models.IntegerField(default=1)
    is_public = models.BooleanField(default=1)
    content = models.TextField(default="")
    tags = TaggableManager()
    memories = models.ManyToManyField(Memory)
    likes = models.ManyToManyField(User, related_name="tip_likes")

    def add_tags(self, tags):
        """
        Purpose:
            Add tags to this Tip

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
            Provide a way for users to 'like' this Tip

        Arguments:
            user -- The Django User instance that likes this Tip
        """

        self.likes.add(user)

    def connect_to_memory(self, memory):
        """
        Purpose:
            Connect this Tip to a relevant memory

        Arguments:
            memory -- The Memory instance that this Tip is related to
        """

        self.memories.add(memory)
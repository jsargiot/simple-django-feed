"""
Simple Activity Feed Models.
"""
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RegisteredUser(models.Model):
    """
    Registered user.

    I've changed a bit the provided model to change the flow of the relationship
    with other registered users. Instead of saying: "Who's tracking me?" I felt
    more comfortable by dealing with: "Who am I tracking?". This change
    improves the form in the admin page so when you add a registered user, you
    add the people he/she is going to track.
    """
    user = models.OneToOneField(User)
    tracking = models.ManyToManyField('self', verbose_name=_("Tracks"),
                                      related_name='tracks', blank=True,
                                      symmetrical=False)

    def __str__(self):
        return str(self.user)


class Ownable(models.Model):
    """
    Ownable.
    Abstract class representing an authored model.
    """
    user = models.ForeignKey(User, verbose_name=_("Author"),
                             related_name="%(class)ss")

    class Meta:
        abstract = True


class FeedItem(Ownable):
    """
    FeedItem.
    Published content of an User.
    """
    content = models.CharField("Content", max_length=1000)

    def __str__(self):
        return str(self.content)

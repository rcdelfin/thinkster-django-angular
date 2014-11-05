from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from authentication.models import UserProfile


class Thought(models.Model):
    author = models.ForeignKey(UserProfile)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{0}'.format(self.content)

    @receiver(pre_delete, sender=UserProfile)
    def delete_thoughts_for_account(sender, instance=None, **kwargs):
        if instance:
            thoughts = Thought.objects.filter(author=instance)
            thoughts.delete()

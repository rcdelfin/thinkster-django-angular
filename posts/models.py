from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from authentication.models import Account


class Post(models.Model):
    author = models.ForeignKey(Account)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{0}'.format(self.content)

    receiver(pre_delete, sender=Account)
    def delete_thoughts_for_profile(sender, instance=None, **kwargs):
        if instance:
            posts = Post.objects.filter(author=instance)
            posts.delete()

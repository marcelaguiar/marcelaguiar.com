from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class CommonInfo(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Created')
    created_by = models.ForeignKey(User, on_delete=models.PROTECT,
                                   related_name='%(app_label)s_%(class)s_created', verbose_name='Created By')
    modified = models.DateTimeField(auto_now=True, verbose_name='Modified')
    modified_by = models.ForeignKey(User, on_delete=models.PROTECT,
                                    related_name='%(app_label)s_%(class)s_modified', verbose_name='Modified By')

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(CommonInfo, self).save(*args, **kwargs)

    class Meta:
        abstract = True

class Post(CommonInfo):
    title = models.CharField(max_length=100, verbose_name="Title")
    subtitle = models.TextField(max_length=1000, blank=True, verbose_name="Subtitle")

    def __str__(self):
        return self.title

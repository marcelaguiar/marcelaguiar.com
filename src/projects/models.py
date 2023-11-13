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

class Project(CommonInfo):
    name = models.CharField(max_length=100, verbose_name="Name")
    description = models.CharField(max_length=250, verbose_name="Description")
    url = models.URLField(default=None, blank=True, null=True, verbose_name="URL")

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_project')
        ]

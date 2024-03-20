from django.contrib.auth.models import User
from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.utils import timezone
from ckeditor.fields import RichTextField


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
    body = RichTextField(default="none", verbose_name="Body")
    slug = models.SlugField(default=None, null=True, blank=True, verbose_name="Slug")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["title"], name="unique_post_title")
        ]

    def __str__(self):
        return self.title

class Subscriber(CommonInfo):
    email = models.EmailField(max_length=254, verbose_name="Email")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["email"], name="unique_subscriber_email")
        ]

    def __str__(self):
        return self.email

@receiver(signal=signals.pre_save, sender=Post)
def Post_create(sender, instance, raw,  *args, **kwargs):
    if instance.pk is None:
        instance.slug = slugify(instance.title)

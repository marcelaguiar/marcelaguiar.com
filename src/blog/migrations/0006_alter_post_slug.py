# Generated by Django 4.2.7 on 2023-11-30 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_uuid_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, default=None, null=True, verbose_name='Slug'),
        ),
    ]

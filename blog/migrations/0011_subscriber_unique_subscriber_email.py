# Generated by Django 4.2.7 on 2024-03-20 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_rename_blogsubscriber_subscriber'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='subscriber',
            constraint=models.UniqueConstraint(fields=('email',), name='unique_subscriber_email'),
        ),
    ]

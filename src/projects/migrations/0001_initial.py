# Generated by Django 4.2.7 on 2023-11-13 05:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(blank=True, max_length=1000, verbose_name='Description')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_modified', to=settings.AUTH_USER_MODEL, verbose_name='Modified By')),
            ],
        ),
        migrations.AddConstraint(
            model_name='projects',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_project'),
        ),
    ]

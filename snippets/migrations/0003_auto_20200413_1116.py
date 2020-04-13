# Generated by Django 3.0.5 on 2020-04-13 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("snippets", "0002_auto_20200405_0930"),
    ]

    operations = [
        migrations.AddField(
            model_name="snippet",
            name="highlighted",
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name="snippet",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="snippets",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]

# Generated by Django 4.2.19 on 2025-03-26 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='preview_content',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Краткое содержание'),
        ),
    ]

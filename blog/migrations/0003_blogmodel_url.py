# Generated by Django 3.0.3 on 2020-08-08 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogmodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]

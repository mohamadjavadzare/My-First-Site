# Generated by Django 3.2.4 on 2023-04-06 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_comment_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='login_require',
            field=models.BooleanField(default=False),
        ),
    ]

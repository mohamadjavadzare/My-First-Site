# Generated by Django 3.2.4 on 2023-04-05 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_alter_contact_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]

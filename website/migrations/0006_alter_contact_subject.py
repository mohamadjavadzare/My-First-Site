# Generated by Django 3.2.4 on 2023-04-05 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_contact_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]

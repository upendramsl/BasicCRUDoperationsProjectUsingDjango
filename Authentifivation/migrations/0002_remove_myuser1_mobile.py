# Generated by Django 5.0.1 on 2024-02-14 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Authentifivation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser1',
            name='mobile',
        ),
    ]

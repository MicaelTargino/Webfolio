# Generated by Django 4.2.9 on 2024-07-26 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactitem',
            name='username',
            field=models.CharField(default='username', max_length=255),
        ),
    ]
# Generated by Django 5.0.6 on 2024-07-03 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicmessage',
            name='created_ad',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

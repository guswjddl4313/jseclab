# Generated by Django 2.2.4 on 2022-08-09 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jhpy', '0008_auto_20220810_0348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='top_fixed',
        ),
    ]
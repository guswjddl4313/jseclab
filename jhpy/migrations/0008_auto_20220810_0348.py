# Generated by Django 2.2.4 on 2022-08-09 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jhpy', '0007_auto_20220810_0327'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='top_fixed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='notice',
            name='top_fixed',
            field=models.BooleanField(default=False),
        ),
    ]
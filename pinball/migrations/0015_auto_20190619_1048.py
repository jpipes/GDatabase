# Generated by Django 2.0.13 on 2019-06-19 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pinball', '0014_auto_20190619_0831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='album',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Track',
        ),
    ]

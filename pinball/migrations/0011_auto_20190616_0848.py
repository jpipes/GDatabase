# Generated by Django 2.0.13 on 2019-06-16 13:48

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pinball', '0010_auto_20190616_0817'),
    ]

    operations = [
        migrations.AddField(
            model_name='repair',
            name='pinball',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pinball.PinballInstance'),
        ),
        migrations.AlterField(
            model_name='repair',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular repair across whole company', primary_key=True, serialize=False),
        ),
    ]
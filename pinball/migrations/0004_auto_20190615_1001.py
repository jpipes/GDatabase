# Generated by Django 2.0.13 on 2019-06-15 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pinball', '0003_auto_20190612_1958'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parts',
            options={'ordering': ['part_number'], 'verbose_name_plural': 'parts'},
        ),
        migrations.AlterField(
            model_name='pinballinstance',
            name='cabinet',
            field=models.CharField(blank=True, choices=[('s', 'Standard Edition'), ('l', 'Limited Edition'), ('p', 'Pro Edition'), ('r', 'Premium Edition')], default='s', help_text='Cabinet Type', max_length=1),
        ),
        migrations.AlterField(
            model_name='pinballinstance',
            name='region',
            field=models.ForeignKey(blank=True, help_text='Select a region for this game', null=True, on_delete=django.db.models.deletion.SET_NULL, to='pinball.Region'),
        ),
    ]
# Generated by Django 2.0.13 on 2019-06-10 03:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a coil model number (e.g. AE-2300-800-01', max_length=100)),
                ('diode', models.BooleanField(default=True, help_text='Does the coil have a diode?')),
                ('primary', models.DecimalField(blank=True, decimal_places=2, help_text='Primary coil resistance', max_digits=4, null=True)),
                ('secondary', models.DecimalField(blank=True, decimal_places=2, help_text='Secondary coil resistance', max_digits=4, null=True)),
                ('cross_ref', models.ManyToManyField(blank=True, help_text='Select the coils that can be subbed with this coil', to='pinball.Coil')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'companies',
                'ordering': ['company_name'],
            },
        ),
        migrations.CreateModel(
            name='Game_Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a game series (e.g. Street Fighter)', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'game series',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a game genre (e.g. Fighting)', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'genres',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a game location (e.g. Richardson, Arlington)', max_length=200)),
                ('short', models.CharField(help_text='Enter an abbreviated name (2 letters)', max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of the part', max_length=200)),
                ('description', models.TextField(blank=True, help_text='Enter the description of the part', max_length=1000, null=True)),
                ('part_number', models.CharField(blank=True, help_text='Enter the part number', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pinball',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(blank=True, help_text='Enter a brief description of the game', max_length=1000, null=True)),
                ('coils', models.ManyToManyField(help_text='Select the coils used in this game', to='pinball.Coil')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pinball.Company')),
                ('game_series', models.ForeignKey(blank=True, help_text='Select a series for this game, or leave blank if it does not belong to a series', null=True, on_delete=django.db.models.deletion.SET_NULL, to='pinball.Game_Series')),
                ('genre', models.ManyToManyField(help_text='Select a genre for this game', to='pinball.Genre')),
                ('parts', models.ManyToManyField(help_text='Add parts specific to this game', to='pinball.Parts')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='PinballInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular game across whole company', primary_key=True, serialize=False)),
                ('sn', models.CharField(blank=True, max_length=100, null=True)),
                ('issues', models.TextField(blank=True, help_text='Enter a brief description of any issues', max_length=1000, null=True)),
                ('last_PM', models.DateField(blank=True, help_text='Date the game was last PMed', null=True)),
                ('cabinet', models.CharField(blank=True, choices=[('l', 'Limited Edition'), ('p', 'Pro Edition'), ('r', 'Premium Edition')], default='p', help_text='Cabinet Type', max_length=1)),
                ('status', models.CharField(blank=True, choices=[('m', 'Maintenance'), ('o', 'On Floor'), ('a', 'Available')], default='a', help_text='Game Status', max_length=1)),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pinball.Pinball')),
                ('location', models.ForeignKey(help_text='Select a location for this game', null=True, on_delete=django.db.models.deletion.SET_NULL, to='pinball.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a game region (e.g. USA, Japan)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Release_Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.DateTimeField()),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Repair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptom', models.CharField(help_text='Describe the issue', max_length=200)),
                ('repair', models.CharField(help_text='Describe the repair', max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='pinballinstance',
            name='region',
            field=models.ForeignKey(help_text='Select a region for this game', null=True, on_delete=django.db.models.deletion.SET_NULL, to='pinball.Region'),
        ),
        migrations.AddField(
            model_name='pinballinstance',
            name='repairs',
            field=models.ForeignKey(blank=True, help_text='Repair logs', null=True, on_delete=django.db.models.deletion.SET_NULL, to='pinball.Repair'),
        ),
        migrations.AddField(
            model_name='pinball',
            name='release',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pinball.Release_Year'),
        ),
    ]

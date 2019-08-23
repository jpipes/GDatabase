""" Included files """

from django.conf import settings
from django.db import models
from django.utils import timezone
import uuid
from django.urls import reverse
import datetime

""" ForeignKey used when directing to another object.
    TextField and Charfield used when directly entering information not used by other models.
    ManyToManyField used when the object can contain multiple other objects. """

""" Year Field Setup """

YEAR_CHOICES = []
for r in range(1975, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))


""" Main objects for pinball database. """ 
class Pinball(models.Model):
    """Model representing a game(but not a specific copy of a Pinball)."""
    title = models.CharField(max_length=200)
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True)
    release = models.IntegerField('Release_Year', choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the game', null=True, blank=True) 
    genre = models.ManyToManyField('Genre', help_text='Select a genre for this game')
    game_series = models.ForeignKey('Game_Series', on_delete=models.SET_NULL, null=True, blank=True, help_text='Select a series for this game, or leave blank if it does not belong to a series')
    coils = models.ManyToManyField('Coil', blank=True, help_text='Select the coils used in this game')
    parts = models.ManyToManyField('Parts', blank=True, help_text='Add parts specific to this game')
    #translite = models.ImageField(upload_to='marquee/', null=True, blank=True, storage=gd_storage)
    #manual = models.FileField(upload_to='manuals/', null=True, blank=True, storage=gd_storage)


    class Meta:
        ordering = ['title']
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this game."""
        return reverse('pinball_detail', args=[str(self.id)])

    
    display_genre.short_description = 'Genre'


class PinballInstance(models.Model):
    """Model representing a specific copy of a game."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular game across whole company')
    sn = models.CharField(max_length=100, blank=True, null=True)
    pinball = models.ForeignKey('Pinball', on_delete=models.SET_NULL, null=True,) 
    location=models.ForeignKey('Location', on_delete=models.SET_NULL, null=True, help_text='Select a location for this game')
    region = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True, blank=True, help_text='Select a region for this game')
    issues=models.TextField(max_length=1000, null=True, blank=True, help_text='Enter a brief description of any issues')
    last_PM=models.DateField(null=True, blank=True, help_text='Date the game was last PMed')
    CAB_TYPE = (
        ('s', 'Standard Edition'),
        ('l', 'Limited Edition'),
        ('p', 'Pro Edition'),
        ('r', 'Premium Edition'),
    )
    cabinet=models.CharField(
        max_length=1,
        choices=CAB_TYPE,
        blank=True,
        default='s',
        help_text='Cabinet Type'
        
    )
    GAME_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On Floor'),
        ('a', 'Available'),
    )
    status = models.CharField(
        max_length=1,
        choices=GAME_STATUS,
        blank=True,
        default='a',
        help_text='Game Status',
    )
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.pinball.title})'

""" Secondary objects for pinball database """

class Company(models.Model):
    """Model representing an company."""
    company_name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "companies"
        ordering = ['company_name']
    def get_absolute_url(self):
        """Returns the url to access a particular company instance."""
        return reverse('company_detail', args=[str(self.id)])
    def __str__(self):
        """String for representing the Model object."""
        return self.company_name

class Release_Year(models.Model):
    """Model representing a game release date."""
    name = models.IntegerField()
    class Meta:
        ordering = ["-name"]
    def get_absolute_url(self):
        return reverse('year_detail')
    """def __str__(self):
        String for representing the Model object.
        return self.name"""

class Genre(models.Model):
    """Model representing a game genre."""
    name = models.CharField(max_length=200, help_text='Enter a game genre (e.g. Fighting)')
    class Meta:
        verbose_name_plural= "genres"
        ordering = ['name']
    def get_absolute_url(self):
        """returns the url to access a particular genre instance."""
        return reverse('genre_detail', arg=[str(self.id)])
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Game_Series(models.Model):
    """Model representing a game series."""
    name = models.CharField(max_length=200, help_text='Enter a game series (e.g. Street Fighter)')
    class Meta:
        verbose_name_plural = "game series"
    def get_absolute_url(self):
        return reverse("series_detail", arg=[str(self.id)])
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Coil(models.Model):
    """Model representing a coil for a pinball"""
    name = models.CharField(max_length=100, help_text='Enter a coil model number (e.g. AE-2300-800-01')
    diode = models.BooleanField(default=True, help_text='Does the coil have a diode?')
    primary = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, help_text='Primary coil resistance')
    secondary = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, help_text='Secondary coil resistance')
    cross_ref = models.ManyToManyField('Coil', blank=True, help_text='Select the coils that can be subbed with this coil')
    def __str__(self):
        return self.name

class Parts(models.Model):
    """Model representing parts for a game"""
    name = models.CharField(max_length=200, help_text='Enter the name of the part')
    description = models.TextField(max_length=1000, null=True, blank=True, help_text='Enter the description of the part')
    part_number = models.CharField(max_length=50, help_text='Enter the part number', null=True, blank=True)
    class Meta:
        verbose_name_plural = 'parts'
        ordering = ['part_number']

    def __str__(self):
        return self.name

class Repair(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular repair across whole company')
    pinball = models.ForeignKey('PinballInstance', on_delete=models.SET_NULL, null=True)
    symptom = models.CharField(max_length=200, help_text='Describe the issue')
    # symptom_image = models.ImageField(upload_to='monitor/symptoms/', null=True, blank=True, storage=gd_storage)
    repair = models.CharField(max_length=500, help_text='Describe the repair')
    date_logged = models.DateTimeField(help_text="Date Logged", null=True, blank=True, default=timezone.now())
    
    def __str__(self):
        return self.symptom
        
class Location(models.Model):
    """Model representing a game location."""
    name = models.CharField(max_length=200, help_text='Enter a game location (e.g. Richardson, Arlington)')
    short = models.CharField(max_length=2, null=True, help_text='Enter an abbreviated name (2 letters)')
    address = models.TextField(null=True, blank=True, help_text='Enter the address')
    class Meta:
        ordering = ["pk"]
    def get_absolute_url(self):
        return reverse('location-detail')
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    

class Region(models.Model):
    """Model representing a game region."""
    name = models.CharField(max_length=200, help_text='Enter a game region (e.g. USA, Japan)')
    def __str__(self):
        """String for representing the Model object."""
        return self.name




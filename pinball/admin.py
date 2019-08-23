from django.contrib import admin

# Register your models here.
from pinball.models import Pinball, PinballInstance, Company, Release_Year, Genre, Game_Series, Coil, Parts, Location, Region, Repair

admin.site.register(Pinball)
admin.site.register(PinballInstance)
admin.site.register(Company)
admin.site.register(Release_Year)
admin.site.register(Genre)
admin.site.register(Game_Series)
admin.site.register(Coil)
admin.site.register(Parts)
admin.site.register(Location)
admin.site.register(Region)
admin.site.register(Repair)
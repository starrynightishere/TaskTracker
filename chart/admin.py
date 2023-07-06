from django.contrib import admin

from . models import data, analysis

# Register your models here.
admin.site.register( data)

admin.site.register(analysis)
from django.contrib import admin
from . models import Personne 

class PersonneAdmin(admin.ModelAdmin):
    list_display = ('nom','prenom','nbre')



admin.site.register(Personne, PersonneAdmin)
# Register your models here.

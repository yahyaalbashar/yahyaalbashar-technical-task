from django.contrib import admin
from .models import Digimon
# Register your models here.

@admin.register(Digimon)
class AdminDigimon(admin.ModelAdmin):
    list_display=["name","level","image"]
    list_display_links=["image"]

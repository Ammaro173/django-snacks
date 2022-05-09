from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Thing


@admin.register(Thing)
class AdminThing(admin.ModelAdmin):
    list_display = ("name", "description", "price", "is_cool")

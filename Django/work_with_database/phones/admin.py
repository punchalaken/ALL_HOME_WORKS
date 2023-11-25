from django.contrib import admin
from .models import Phone


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'release_date', 'lte_exist',  'slug')
    list_filter = ('name', 'price', 'release_date', 'lte_exist',  'slug')
    prepopulated_fields = {"slug": ("name", )}

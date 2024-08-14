from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Item

# Register your models here.

@admin.register(Item)
class ItemAdmin(ImportExportModelAdmin):
    list_display = ('name', 'description', 'code', 'quantity','price','vendor')
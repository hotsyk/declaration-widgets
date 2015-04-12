from django.contrib import admin

from .models import DeclarationStore


@admin.register(DeclarationStore)
class DeclarationStoreAdmin(admin.ModelAdmin):
    pass

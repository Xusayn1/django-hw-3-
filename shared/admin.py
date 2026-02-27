from django.contrib import admin

# Register your models here.

from shared.models import Contact 

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'created_at', 'is_read')
    search_fields = ('full_name', 'email', 'subject')
    list_filter = ('created_at','is_read')
from django.contrib import admin

from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'hire_date', 'email', 'is_mvp')
    list_display_links = ('id', 'name')
    list_filter = ('hire_date',)
    list_editable = ('is_mvp',)
    search_fields = ('name', 'description', 'email',)
    list_per_page = 25

admin.site.register(Realtor, RealtorAdmin)
from django.contrib import admin
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('parent_name', 'parent_email', 'student_age', 'created_at')
    readonly_fields = ('created_at',)

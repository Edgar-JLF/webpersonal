from django.contrib import admin
from .models import Courses, About

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(About, AboutAdmin)
admin.site.register(Courses, ServiceAdmin)
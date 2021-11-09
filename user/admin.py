from django.contrib import admin
from .models import CustomUser



@admin.register(CustomUser)
class UserDisplay(admin.ModelAdmin):
    list_display= ('id', 'phone', 'email', 'username', 'date_joined')
    search_fields= ('email', 'phone')

from django.contrib import admin

from .models import Content, Section, Cv, Post, PostSection, PostParagraph

#https://realpython.com/customize-django-admin-python/


# @admin.register(Content)
# class ContentDisplay(admin.ModelAdmin):
#     list_display= ('')


# @admin.register(Section)
# class SectionDisplay(admin.ModelAdmin):
#     list_display= ()


# @admin.register(Cv)
# class CvDisplay(admin.ModelAdmin):
#     list_display= ('section',)

array = [Section, Content, Cv, Post, PostSection, PostParagraph]
admin.site.register(array)

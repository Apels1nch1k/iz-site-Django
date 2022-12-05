from django.contrib import admin
from .models import *
# Register your models here.
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','content', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    


admin.site.register(Application, ApplicationAdmin)
admin.site.register(Category, CategoryAdmin)
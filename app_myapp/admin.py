from django.contrib import admin
from . import models
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('name','viewscounter','created_at')
    search_fields = ('name','content')

admin.site.register(models.Post,PostAdmin)
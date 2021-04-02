from django.contrib import admin
from .models import Recipe, Note, Tool
# Register your models here.
admin.site.register(Recipe)
admin.site.register(Note)
admin.site.register(Tool)
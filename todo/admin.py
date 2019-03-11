from django.contrib import admin
from .models import ToDo
# Register your models here.
class TodoListAdmin(admin.ModelAdmin):
    list_display = ("name","duedate")

admin.site.register(ToDo,TodoListAdmin)

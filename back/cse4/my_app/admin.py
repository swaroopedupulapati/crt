from django.contrib import admin

# Register your models here.
from .models import Book

@admin.register(Book)
class RegisterBook(admin.ModelAdmin):
    list_display = ("title", "author")


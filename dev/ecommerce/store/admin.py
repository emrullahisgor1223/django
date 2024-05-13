from django.contrib import admin

# Register your models here.

from .models import Category,product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    prepopulated_fields={'slug':('name',)}

@admin.register(product)
class productAdmin(admin.ModelAdmin):

    prepopulated_fields={'slug':('title',)}
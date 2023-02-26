from django.contrib import admin
from webapp.models import Category, Product


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'description')
    list_filter = ('id', 'category')
    search_fields = ('id', 'category', 'description')
    fields = ('id', 'category', 'description')
    readonly_fields = ('id', 'category', 'description')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_id', 'description', 'added_at', 'coast', 'image')
    list_filter = ('id', 'category_id', 'description', 'added_at', 'coast')
    search_fields = ('id', 'category_id', 'description', 'added_at', 'coast')
    fields = ('id', 'category_id', 'description', 'added_at', 'coast', 'image')
    readonly_fields = ('id', 'category_id', 'description', 'added_at', 'coast', 'image')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

from django.contrib import admin
from lachesis.models import Category, Page

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', )}

admin.site.register(Category)
admin.site.register(Page)
admin.site.register(Category, CategoryAdmin)

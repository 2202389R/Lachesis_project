from django.contrib import admin
from lachesis.models import Genre, Story
from lachesis.models import UserProfile

class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'url')

class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Genre, GenreAdmin)
admin.site.register(Story, StoryAdmin)
admin.site.register(UserProfile)

from django.contrib import admin
from lachesis.models import Genre, Story, Segment
from lachesis.models import UserProfile

class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', )}

class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'author')

class SegmentAdmin(admin.ModelAdmin):
    list_display = ('story', 'closed')

admin.site.register(Genre, GenreAdmin)
admin.site.register(Story, StoryAdmin)
admin.site.register(Segment, SegmentAdmin)
admin.site.register(UserProfile)

from django.contrib import admin

from .models import Song, Program, Composer, ProgramSong, Artist


class ProgramSongInline(admin.StackedInline):
    model = ProgramSong
    extra = 3


class ProgramAdmin(admin.ModelAdmin):
    inlines = [ProgramSongInline]


admin.site.register(Song)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Composer)
admin.site.register(Artist)


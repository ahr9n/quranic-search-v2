from django.contrib import admin
from .models import Verses, Surah

admin.site.site_header = 'Quranic Lexical Search API'
admin.site.site_title = 'Quranic Lexical Search API'


# Register your models here.


@admin.register(Verses)
class ModelVerses(admin.ModelAdmin):
    list_display = ['__str__', 'verse_pk', 'surah', 'numberInQuran', 'page', 'hizbQuarter', 'juz', 'sajda']
    list_filter = ['surah', 'juz', 'hizbQuarter', 'page', 'sajda']
    search_fields = ['verse', 'verseWithoutTashkeel']


@admin.register(Surah)
class ModelSurah(admin.ModelAdmin):
    list_display = ['name', 'nameWithoutTashkeel']
    search_fields = ['name', 'nameWithoutTashkeel']

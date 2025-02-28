from django.urls import path

from .views import *

app_name = "QuranLexicalSearchAPI"

urlpatterns = [
    # API views
    path("", api_docs, name="api_docs"),
    path("api/lexical/all", get_all, name="get_all"),
    path("api/lexical/search/<str:words>", search, name="search"),
    path("api/lexical/surah/<int:surah_id>", get_surah, name="get_surah"),
    path(
        "api/lexical/verse-in-surah/<int:surah_id>/<int:verse_id>",
        get_verse_in_surah,
        name="get_verse_in_surah",
    ),
    path(
        "api/lexical/verse-in-quran/<int:verse_id>",
        get_verse_in_quran,
        name="get_verse_in_quran",
    ),
]

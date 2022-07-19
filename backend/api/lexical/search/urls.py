from django.urls import path
from .views import *

app_name = 'QuranAPI'

urlpatterns = [
    # API views
    path('', api_docs, name='api_docs'),
    path('api/lexical/all-verses', all_verses_api, name='all_verses_api'),
    path('api/lexical/search-word/<str:words>', search_word_api, name='search_word_api'),
    path('api/lexical/get-surah/<int:surah_id>', get_surah_api, name='get_surah_api'),
    path('api/lexical/get-verse/<int:surah_id>/<int:verse_id>', get_verse_api, name='get_verse_api'),
]

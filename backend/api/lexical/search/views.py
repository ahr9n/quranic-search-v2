from .models import Verses
from .serializers import VersesSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q
from django.shortcuts import get_object_or_404, render


@api_view(['GET'])
def all_verses_api(request) -> None:
    """
        Returns all verses in Database.
        Not really effective for search, so use it to clone the database or such on.
    """
    verses = Verses.objects.all()
    data = VersesSerializers(verses, many=True).data
    print(verses)
    print(data)
    return Response({'length': len(data), 'data': data})


@api_view(['GET'])
def search_word_api(request, words) -> str:
    """
        Search in verses using icontains.
        Return all verses with given words.
    """
    verses = Verses.objects.filter(
        Q(verse__icontains=words) | Q(verseWithoutTashkeel__icontains=words)
    )
    data = VersesSerializers(verses, many=True).data
    return Response({'resultsLength': len(data), 'data': data})


@api_view(['GET'])
def get_surah_api(request, surah_id) -> int:
    """
        Retrieving surah_pk, searching in database with verse_pk:
        verse_pk: S***V*** | surah_pk -> first part of verse_pk (S***).
        Returns all Verses of Surah.
    """
    surah_pk = f"S{str(surah_id).zfill(3)}"
    verse_id = Verses.objects.filter(verse_pk__icontains=surah_pk)
    data = VersesSerializers(verse_id, many=True).data
    return Response({'versesNumber': len(data), 'data': data})


@api_view(['GET'])
def get_verse_api(request, surah_id, verse_id) -> int:
    """
        Taking two integers and convert them to verse_pk,
        to search in database with it using get_object_or_404.
        Returns the Verse.
    """
    verse_pk = f'S{str(surah_id).zfill(3)}V{str(verse_id).zfill(3)}'
    verse = get_object_or_404(Verses, verse_pk=verse_pk)
    data = VersesSerializers(verse).data
    return Response({'data': data})


def api_docs(request):
    return render(request, 'search/api.html')

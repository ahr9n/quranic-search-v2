from rest_framework import serializers
from .models import Verses


class VersesSerializers(serializers.ModelSerializer):
    # surah = serializers.SerializerMethodField(source='get_surah_name')
    surah = serializers.StringRelatedField()

    class Meta:
        model = Verses
        fields = [
            'verse_pk',
            'page',
            'hizbQuarter',
            'juz',
            'surah',
            'verse',
            'verseWithoutTashkeel',
            'numberInSurah',
            'numberInQuran',
            'audio',
            'audio1',
            'audio2',
            'sajda',
        ]

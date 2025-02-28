from django.db import models

# Create your models here.


class Verses(models.Model):
    verse_pk = models.CharField(
        max_length=8, null=False, blank=False, unique=True, verbose_name="مفتاح الآية"
    )
    page = models.PositiveIntegerField(null=False, blank=False, verbose_name="الصفحة")
    hizbQuarter = models.PositiveIntegerField(
        null=False, blank=False, verbose_name="الربع"
    )
    juz = models.PositiveIntegerField(null=False, blank=False, verbose_name="الجزء")
    surah = models.ForeignKey(
        "Surah",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="surah",
        verbose_name="السورة",
    )
    verse = models.CharField(
        max_length=5000, null=False, blank=False, verbose_name="الآية"
    )
    verseWithoutTashkeel = models.CharField(
        max_length=1000, null=False, blank=False, verbose_name="الآية بدون تشكيل"
    )
    numberInSurah = models.PositiveIntegerField(
        null=False, blank=False, verbose_name="رقم الآية في السورة"
    )
    numberInQuran = models.PositiveIntegerField(
        null=False, blank=False, unique=True, verbose_name="رقم الآية في القرءان"
    )
    audio = models.URLField(
        null=False, blank=False, unique=True, verbose_name="مصدر تلاوة أساسي"
    )
    audio1 = models.URLField(
        null=True, blank=True, unique=True, verbose_name="مصدر تلاوة ثانوي 1"
    )
    audio2 = models.URLField(
        null=True, blank=True, unique=True, verbose_name="مصدر تلاوة ثانوي 2"
    )
    sajda = models.BooleanField(verbose_name="هل الآية تحتوي علي سجدة")

    class Meta:
        ordering = ["id"]
        verbose_name = "آية"
        verbose_name_plural = "الآيات"

    def __str__(self):
        return self.verse[:50]


class Surah(models.Model):
    name = models.CharField(max_length=50, verbose_name="اسم السورة")
    nameWithoutTashkeel = models.CharField(
        max_length=30, verbose_name="اسم السورة بدون تشكيل"
    )

    class Meta:
        ordering = ["id"]
        verbose_name = "سورة"
        verbose_name_plural = "السور"

    def __str__(self):
        return self.name

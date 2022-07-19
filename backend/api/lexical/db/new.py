import sqlite3

quran_db = sqlite3.connect('../db/quran.db')
quran_cr = quran_db.cursor()

for i in range(1, 6237):
    id = i
    page = quran_cr.execute(f'SELECT page FROM verses WHERE id == {id}').fetchall()[0][0]
    hizb_quarter = quran_cr.execute(f'SELECT hizbQuarter FROM verses WHERE id == {id}').fetchall()[0][0]
    juz = quran_cr.execute(f'SELECT juz FROM verses WHERE id == {id}').fetchall()[0][0]
    surah = quran_cr.execute(f'SELECT surah FROM verses WHERE id == {id}').fetchall()[0][0]
    verse = quran_cr.execute(f'SELECT verse FROM verses WHERE id == {id}').fetchall()[0][0]
    verse_without_tashkeel = quran_cr.execute(f'SELECT verseWithoutTaskeel FROM verses WHERE id == {id}').fetchall()[0][0]
    number_in_surah = quran_cr.execute(f'SELECT numberInSurah FROM verses WHERE id == {id}').fetchall()[0][0]
    number_in_quran = quran_cr.execute(f'SELECT numberInQuran FROM verses WHERE id == {id}').fetchall()[0][0]
    audio = quran_cr.execute(f'SELECT audio FROM verses WHERE id == {id}').fetchall()[0][0]
    audio1 = quran_cr.execute(f'SELECT audio1 FROM verses WHERE id == {id}').fetchall()[0][0]
    audio2 = quran_cr.execute(f'SELECT audio2 FROM verses WHERE id == {id}').fetchall()[0][0]
    sajda = quran_cr.execute(f'SELECT sajda FROM verses WHERE id == {id}').fetchall()[0][0]
    verse_pk = f'S{str(surah).zfill(3)}V{str(number_in_surah).zfill(3)}'

    django_db = sqlite3.connect('db.sqlite3')
    cr = django_db.cursor()
    cr.execute(
        f'''INSERT INTO search_verse(verse_pk, page, hizbQuarter, juz, verse, verseWithoutTaskeel, numberInSurah,
        numberInQuran, audio, audio1, audio2, sajda) 
        VALUES ("{verse_pk}", {page}, {hizb_quarter}, {juz}, "{verse}", "{verse_without_tashkeel}", {number_in_surah},
        {number_in_quran}, "{audio}", "{audio1}", "{audio2}", {sajda})''')

    django_db.commit()

    print('=' * 50)
    print(verse_pk, '|', page, '|', hizb_quarter, '|', juz, '|', surah, '|', verse, '|', verse_without_tashkeel, '|',
          number_in_surah, '|', number_in_quran, '|', audio, '|', audio1, '|', audio2, '|', sajda)

django_db.close()

# use pyarabic module for cleaning Arabic Words
from pyarabic.araby import strip_tashkeel, strip_diacritics, strip_tatweel
from string import punctuation

def clean_word(word):
  '''
  Get the clean word from the given word, according to the following rules.
  1. Remove tashkeel
  2. Remove diacritics
  3. Remove punctuation
  4. Remove tatweel

  @param word: the word to clean
  @type word: str
  @return: the clean word
  @rtype: str
  '''


  arabic_punctuations = '''`÷×؛<>_()*&^%][ـ،/:"؟.,'{}~¦+|!”…“–ـ'''
  english_punctuations = punctuation
  punctuations_list = arabic_punctuations + english_punctuations

  search  = ["أ", "إ", "آ", "ة", " ", "-", "/", ".", "،", " و ", " يا ",
            '"', "ـ", "'", "ى", "\\", '\n', '\t', '&quot;', '?', '؟', '!', '»', '«']
  replace = ["ا", "ا", "ا", "ه", " ", " ", "", "", "", " و", " يا",
            "", "", "", "ي", "", ' ', ' ', ' ', ' ? ', ' ؟ ', ' ! ', '', '']
  
  word = strip_tashkeel(word)
  word = strip_diacritics(word)
  word = strip_tatweel(word)

  word = word.replace('وو', 'و')
  word = word.replace('يي', 'ي')
  word = word.replace('اا', 'ا')

  for i in range(0, len(search)):
    word = word.replace(search[i], replace[i])

  # clean punctuations
  for i in word:
    if(i in punctuations_list):
      word = word.replace(i,'')
  
  word = word.strip()
  return word
  
def get_quran_clean_text():
  '''
  Get the clean text from quran text, according to the above rules.

  @return: the clean text
  @rtype: list of strings
  '''

  # prepare/read Quran data
  quran_clean_text = open("./data/external/quran-simple-clean.txt").readlines()
  
  # use this instead to display well-formed verses
  # quran_simple = open("quran-simple.txt").readlines()
  
  quran_clean_text = [clean_word(verse[:-1]) for verse in quran_clean_text]
  
  return quran_clean_text
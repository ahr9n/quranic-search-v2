# use pyarabic module for cleaning Arabic Words
from pyarabic.araby import strip_tashkeel, strip_diacritics, strip_tatweel, tokenize
from string import punctuation

def clean(text, model_name):
  '''
  Get the clean word from the given word, according to the following rules.
  1. Remove tashkeel/diacritics/punctuation/tatweel
  
  @param text: the text to clean
  @type text: str
  @return: the clean text
  @rtype: list
  '''

  arabic_punctuations = '''`÷×؛<>_()*&^%][ـ،/:"؟.,'{}~¦+|!”…“–ـ'''
  english_punctuations = punctuation
  punctuations_list = (arabic_punctuations + english_punctuations).replace('_', '')
  
  text = strip_tashkeel(text)
  text = strip_diacritics(text)
  text = strip_tatweel(text)

  if model_name in ['TWITTER', 'WIKI']:
    # skip under_score
    search  = \
    ["أ", "إ", "آ", "ة", " ", "-", "/", ".", "،", " و ", " يا ", '"', "'", "ى", "\\", '\n' , '\t' , '&quot;',  '?',   '؟',   '!', '»', '«']
    replace = \
    ["ا", "ا", "ا", "ه", " ", " ",  "",  "",  "",  " و",  " يا",  "",  "", "ي",   "",       ' ',  ' ',  ' ', ' ? ', ' ؟ ', ' ! ',  '', '' ]
    text = text.replace('وو', 'و')
    text = text.replace('يي', 'ي')
    text = text.replace('اا', 'ا')
    for i in range(0, len(search)):
      text = text.replace(search[i], replace[i])     
  
  if model_name != 'TWITTER':
    text = text.replace('_', '')  
  
  # clean punctuations
  for i in text:
    if(i in punctuations_list):
      text = text.replace(i,'')
  
  # tokenize
  text = tokenize(text)
  return text
    
def get_quran_clean_text():
  '''
  Get the clean text from quran text, according to the above rules.

  @return: the clean text
  @rtype: list of strings
  '''

  # prepare/read Quran data
  quran_clean_text = open("./data/external/quran-simple-clean.txt").readlines()
  quran_clean_text = [verse[:-1] for verse in quran_clean_text]

  return quran_clean_text
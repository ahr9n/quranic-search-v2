from gensim.models import KeyedVectors, Word2Vec
from pyarabic.araby import tokenize
from .preprocess import clean_word, get_quran_clean_text

# model_ksucca = KeyedVectors.load("./references/model.pkl")
model_ksucca = KeyedVectors.load_word2vec_format('./data/processed/ksucca_full_cbow.bin', binary=True)
model_tw = Word2Vec.load('./references/full_grams_cbow_100_twitter.mdl').wv
model_wiki = Word2Vec.load('./references/full_grams_cbow_100_wiki.mdl').wv 

quran_clean_text = get_quran_clean_text()


def get_verse_max_score(query_word, verse_text, model):
    '''
    Get the max similarity of query word and each word in a verse text.

    Example:
    >>> query_word = "الصلاة" 
    >>> verse_text = "صلاة القيام"
    >>> get_verse_max_score(query_word, verse_text, model_ksucca)
    0.5794443
    >>> model.similarity("الصلاة", "صلاة")
    0.5794443
    >>> model.similarity("الصلاة", "القيام")
    0.34846973

    @param query_word: only one query word
    @param verse_text: verse text (one or more words)
    @type query_word, verse_text: str (arabic unicode)
    @param model: the pretrained model to use
    @type model: KeyedVectors or Word2Vec
    @return: max similarity
    @rtype: float
    '''

    maxi = -1.0
    for verse_word in verse_text:
        if query_word not in model or verse_word not in model:
            continue
        score = model.similarity(query_word, verse_word)
        maxi = max(score, maxi)
    
    return max(0.0, maxi)


def get_verse_frequency_score(query_word, verse_text, model):
    '''
    Get the frequency of a query word in a verse with:
    the similarity score higher than 0.3, the more frequent the word is in the verse.

    Example:
    >>> query_word = "الصلاة"
    >>> verse_text = "صلاة القيام"
    >>> get_verse_frequency_score(query_word, verse_text, model_ksucca)
    2

    @param query_word: only one query word
    @param verse_text: verse text (one or more words)
    @type query_word, verse_text: str (arabic unicode)
    @param model: the pretrained model to use
    @type model: KeyedVectors or Word2Vec
    @return: frequency score
    @rtype: int
    '''

    freq = 0
    for verse_word in verse_text:
        if query_word not in model or verse_word not in model:
            continue
        score = model.similarity(query_word, verse_word)
        if score > 0.3:
            freq += 1

    return freq


def get_verse_avg_score(query_word, verse_text, model):
    '''
    Get the average similarity of query word and each word in a verse text.

    Example:
    >>> query_word = "الصلاة"
    >>> verse_text = "صلاة القيام"
    >>> get_avg_score(query_word, verse_text, model_ksucca)
    0.5794443
    >>> (0.5794443 + 0.34846973) / 2.0
    0.463957015

    @param query_word: only one query word
    @param verse_text: verse text (one or more words)
    @type query_word, verse_text: str (arabic unicode)
    @param model: the pretrained model to use
    @type model: KeyedVectors or Word2Vec
    @return: average similarity
    @rtype: float
    '''

    verse_vector = []
    for verse_word in verse_text:
        if query_word not in model or verse_word not in model:
            continue
        score = model.similarity(query_word, verse_word)

        # Ignore negative scores
        if score > 0:
            verse_vector.append(score)

    # Avoid division by zero
    if len(verse_vector) == 0:
        return 0.0

    avg = sum(verse_vector) / len(verse_vector)
    return avg


def get_most_similar_verses(query_word, model, method):
    '''
    Get the most similar verses to a query word,
    according to one model and one of the 3 maximizing methods (max, freq, avg).

    Example:
    >>> get_most_similar_verses(u"هدوء", model_ksucca, get_verse_avg_score)[0]
    (0.2972675710916519, 5680, 'وجعلنا نومكم سباتا')
    >>> get_most_similar_verses(clean_word("هدوء"), model_ksucca, get_verse_frequency_score)[:3]
    [(2, 2901, 'وهو الذي جعل لكم الليل لباسا والنوم سباتا وجعل النهار نشورا'),
     (1, 5817, 'والصبح اذا تنفس'),
     (1, 5680, 'وجعلنا نومكم سباتا')]

    @param query_word: only one query word  
    @type query_word: str (arabic unicode)
    @param model: the pretrained model to use
    @type model: KeyedVectors or Word2Vec
    @param method: the maximizing method to use
    @type method: function
    @return: most similar verses
    @rtype: list of tuples (score, verse_id, verse_text)
    '''

    verse_props, verse_id = [], 0
    for verse in quran_clean_text:
        # Tokenizing and cleaning are made only once :)
        score = method(clean_word(query_word), tokenize(verse), model)
        verse_props.append((score, verse_id))
        verse_id += 1

    verse_props.sort(reverse=True)

    # Return at most 50 verses
    max_out_length = min(len(verse_props), 50)
    most_similar_verses = [(score, verse_id, quran_clean_text[verse_id])
                           for score, verse_id in verse_props[:max_out_length]]
    return most_similar_verses


def get_most_similar_verses_by_query_text(query_text, model, method):
    '''
    Get the most similar verses to a query text,
    according to one model and one of the 3 maximizing methods (max, freq, avg).

    Example:
    >>> query_text = "مثوى الكافرين"
    >>> get_most_similar_verses_by_query_text(query_text, model_ksucca, get_verse_avg_score)[:5]
    [(0.5610717423260212, 5504, 'علي الكافرين غير يسير'),
     (0.47719616691271466, 2332, 'الم تر انا ارسلنا الشياطين علي الكافرين تؤزهم ازا'),
     (0.4661228557427724, 4043, 'الا ابليس استكبر وكان من الكافرين'),
     (0.4329271502792835, 5947, 'فمهل الكافرين امهلهم رويدا'),
     (0.42426673509180546, 1177, 'ذلكم وان الله موهن كيد الكافرين')]

    @param query_text: query text (one or more words)
    @type query_text: str (arabic unicode)
    @param model: the pretrained model to use
    @type model: KeyedVectors or Word2Vec
    @param method: the maximizing method to use
    @type method: function
    @return: most similar verses
    @rtype: list of tuples (score, verse_id, verse_text)
    '''

    # Generalized and better than the split method
    query_text = tokenize(query_text)

    # Feature: Comparing a query word of one 'صلاة' or two concatenated words 'صلاة_القيام',
    # with a verse word of one or two concatenated words

    verse2score = {}
    for i in range(len(query_text)):
        most_similar_verses1 = get_most_similar_verses(
            clean_word(query_text[i]), model, method)
        for score, verse_id, verse in most_similar_verses1:
            # Doubling the score for the frequent results
            if verse_id in verse2score:
                verse2score[(verse_id, verse)] += score
            else:
                verse2score[(verse_id, verse)] = score

        if i + 1 != len(query_text):
            term = clean_word(query_text[i]) + \
                "_" + clean_word(query_text[i + 1])
            most_similar_verses2 = get_most_similar_verses(term, model, method)

            for score, verse_id, verse in most_similar_verses2:
                if verse_id in verse2score:
                    verse2score[(verse_id, verse)] += score
                else:
                    verse2score[(verse_id, verse)] = score

    best_verses = [(score, verse_id, verse)
                   for (verse_id, verse), score in verse2score.items()]
    best_verses.sort(reverse=True)

    # Return at most 50 verses
    max_out_length = min(len(best_verses), 50)
    return best_verses[:max_out_length]


def get_combined_models_results(query_text, method):
    '''
    Get the most similar verses to a query text,
    according to all models and one of the 3 maximizing methods (max, freq, avg).

    Example:
    >>> get_combined_models_results(u"هدوء", get_verse_max_score)[:5]
    [(0.53681993, 3693, 'وقالوا الحمد لله الذي اذهب عنا الحزن ان ربنا لغفور شكور'),
     (0.53681993, 1679, 'وتولي عنهم وقال يااسفي علي يوسف وابيضت عيناه من الحزن فهو كظيم'),
     (0.5333835, 80, 'ثم قست قلوبكم من بعد ذلك فهي كالحجاره او اشد قسوه وان من الحجاره لما يتفجر منه الانهار وان منها لما يشقق فيخرج منه الماء وان منها لما يهبط من خشيه الله وما الله بغافل عما تعملون'),
     (0.5307898, 3261, 'واصبح فؤاد ام موسي فارغا ان كادت لتبدي به لولا ان ربطنا علي قلبها لتكون من المؤمنين'),
     (0.5268251, 1767, 'مثل الذين كفروا بربهم اعمالهم كرماد اشتدت به الريح في يوم عاصف لا يقدرون مما كسبوا علي شيء ذلك هو الضلال البعيد')]

    @param query_text: query text (one or more words)
    @type query_text: str (arabic unicode)
    @param method: the maximizing method to use
    @type method: function
    @return: most similar verses
    @rtype: list of tuples (score, verse_id, verse_text)
    '''

    verse2score = {}
    for model in [model_wiki, model_tw, model_ksucca]:
        score2verse = get_most_similar_verses_by_query_text(
            query_text, model, method)

        for score, verse_id, verse in score2verse:
            if verse in verse2score:
                verse2score[(verse_id, verse)] += score
            else:
                verse2score[(verse_id, verse)] = score

    best_score2verse = [(score, verse_id, verse)
                          for (verse_id, verse), score in verse2score.items()]
    best_score2verse.sort(reverse=True)

    # Return at most 50 verses
    max_out_length = min(len(best_score2verse), 50)
    return best_score2verse[:max_out_length]


def get_all_combined(query_text):
    '''
    Get the most similar verses to a query text,
    based on combining all models with all maximizing methods.

    @param query_text: query text (one or more words)
    @type query_text: str (arabic unicode)
    @return: most similar verses
    @rtype: list of tuples (score, verse_id, verse_text)
    '''

    methods = [get_combined_models_results(query_text, get_verse_max_score),
               get_combined_models_results(
                   query_text, get_verse_frequency_score),
               get_combined_models_results(query_text, get_verse_avg_score)]

    # To have a constant measurement, scores are defined based on sum of all scores
    max_score = [sum([score for score, verse_id, verse in method])
                 for method in methods]

    verse2score = {}
    for i in range(3):
        for score, verse_id, verse in methods[i]:
            final_score = score / max_score[i]

            # Avoid division by zero
            if final_score == 0:
                continue

            if (verse_id, verse) in verse2score:
                verse2score[(verse_id, verse)][0] += final_score
                verse2score[(verse_id, verse)][1] += 1.0
            else:
                verse2score[(verse_id, verse)] = [final_score, 1.0]

    score2verse = []
    for (verse_id, verse), [score, frequency] in verse2score.items():
        score2verse.append((score / frequency, verse_id, verse))

    score2verse.sort(reverse=True)

    # Return at most 50 verses
    max_out_length = min(len(score2verse), 50)
    return score2verse[:max_out_length]

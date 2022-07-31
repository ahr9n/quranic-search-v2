from requests import get
from flask import jsonify, make_response
from flask_restful import Resource
from gensim.models import KeyedVectors, Word2Vec
from .preprocess import *
from .semantic_methods import * 
from .pooling import *

# model_wiki = Word2Vec.load('../../models/full_grams_cbow_300_wiki.mdl').wv 
# model_tw = Word2Vec.load('../../models/full_grams_cbow_300_twitter.mdl').wv
# model_ksucca = KeyedVectors.load_word2vec_format('../../data/processed/ksucca_full_cbow.bin', binary=True)
model_ksucca = KeyedVectors.load("../../models/model.pkl")
# model_fasttext = KeyedVectors.load_word2vec_format("../../models/cc.ar.300.vec")

quran_clean_text = get_quran_clean_text()

def fetch(verse_ids):
    output = []
    for id in verse_ids:
        url = f"http://localhost:8000/api/lexical/verse-in-quran/{id}"
        headers = {'content-type': 'application/json'}
        results = get(url, headers=headers)
        results = results.json()
        output.append(results['data'])
    return output

class MostSimilarWord(Resource):

    def get(self, word):
        '''Outputs the 100 most similar words [from the Holy Quran],
        besides their relative similarity scores for the given word.

        @param word: the word to use
        @type word: str
        @return: the 100 most similar words from the Holy Quran] + similarity scores
        @rtype: list of tuples (score, word)
        '''

        word = clean(word, 'KSUCCA')
        if len(word):
            word = word[0]
        else:
            return make_response(jsonify({'error': 'No word provided'}), 400)

        word_scores = []
        for verse_text in quran_clean_text:
            for verse_word in verse_text.split():
                cleaned_verse_word = clean(verse_word, 'KSUCCA')[0]
                if cleaned_verse_word in model_ksucca and word in model_ksucca and cleaned_verse_word != word:
                    score = model_ksucca.similarity(word, cleaned_verse_word)
                    word_scores.append((score, verse_word))
        word_scores.sort(reverse=True)

        out = word_scores[:min(len(word_scores), 100)]

        # Fixing: TypeError(Object of type float32 is not JSON serializable)
        for idx, (score, verse_word) in enumerate(out):
            tmp = (float(score), verse_word)
            out[idx] = tmp

        return make_response(jsonify({'results': out}), 200)


class MostSimilarVerse(Resource):

    def get(self, query):
        '''Outputs the 10 most similar words from the Holy Quran,
        besides their relative frequency scores for the given query.

        @param query: the query to use
        @type query: str
        @return: props of the most similar verses from the Holy Quran
        @rtype: list of tuples (score, verse_id, verse)
        '''
        
        results = get_most_similar_verses_by_query_text(query, (model_ksucca, 'KSUCCA'), get_verse_max_score)

        # Fixing: TypeError(Object of type float32 is not JSON serializable)
        for idx, (score, verse_id, verse) in enumerate(results):
            tmp = (float(score), verse_id, verse)
            results[idx] = tmp

        print(results[:3])

        results = [verse_id+1 for score, verse_id, verse in results]
        results = fetch(results)

        return make_response(jsonify({'length': len(results), 'data': results}), 200)
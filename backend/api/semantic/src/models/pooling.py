from .preprocess import clean, get_quran_clean_text
from pyarabic.araby import tokenize
import numpy as np

quran_clean_text = get_quran_clean_text()

def get_max_pooling_vec(query_text, model):
    '''
    Get the max pooling vector for the given tokens.

    @param query_text: list of words
    @type query_text: list
    @param model: tuple of the pre-trained model to use and its name
    @type model: Word2Vec or KeyedVectors
    @return: max pooling vector
    @rtype: numpy array
    '''

    # Warning: checkout the shape of the vectors
    arr = [-1e9 for idx in range(300)]
    max_pooling_vec = np.copy(np.array(arr))  # avoid read-only error

    (model_vectors, model_name) = model

    for token in query_text:
        cleaned = clean(token, model_name)
        if len(cleaned):
            cleaned = cleaned[0]
        else:
            cleaned = ''

        if cleaned not in model_vectors:
            continue
        
        vec = model_vectors[cleaned]
        for idx in range(300):
            max_pooling_vec[idx] = max(max_pooling_vec[idx], vec[idx])

    return max_pooling_vec


def get_avg_pooling_vec(query_text, model):
    '''
    Get the average pooling vector for the given tokens.

    @param query_text: list of words
    @type query_text: list
    @param model: tuple of the pre-trained model to use and its name
    @type model: Word2Vec or KeyedVectors
    @return: average pooling vector
    @rtype: numpy array
    '''

    # Warning: checkout the shape of the vectors
    arr = [0 for idx in range(300)]
    avg_pooling_vec = np.copy(np.array(arr))  # avoid read-only error

    cnt = 0
    (model_vectors, model_name) = model
    
    for token in query_text:
        cleaned = clean(token, model_name)
        if len(cleaned):
            cleaned = cleaned[0]
        else:
            cleaned = ''
        
        if cleaned not in model_vectors:
            continue   
        
        cnt += 1
        vec = model_vectors[cleaned]
        for idx in range(300):
            avg_pooling_vec[idx] += vec[idx]

    for idx in range(300):
        avg_pooling_vec[idx] /= max(1, cnt)
    
    return avg_pooling_vec


def get_pooling_results(query_text, model, method):
    '''
    Get the pooling results for the given tokens,
    according to the given model and method.

    @param query_text: list of words
    @type query_text: list
    @param model: tuple of the pre-trained model to use and its name
    @type model: Word2Vec or KeyedVectors
    @param method: the method to use
    @type method: function
    @return: most similar verses
    @rtype: list of tuples (score, verse_id, verse)
    '''

    query_method_pooling_vec = method(query_text, model)

    verse_scores, verse_id = [], 0
    for verse in quran_clean_text:
        verse_method_pooling_vec = method(verse, model)
        cosine_similarity = np.dot(query_method_pooling_vec, verse_method_pooling_vec) / (
            np.linalg.norm(query_method_pooling_vec) * np.linalg.norm(verse_method_pooling_vec))

        # score = model_vectors.similarity(query_max_pooling_vec, verse_max_pooling_vec)
        # will fail, because we generated new vectors that doesn't belong to any model
        verse_scores.append((cosine_similarity, verse_id))
        verse_id += 1

    verse_scores.sort(reverse=True)

    # Return at most 50 verses
    max_out_length = min(len(verse_scores), 50)
    most_similar_verses = [(score, verse_id, quran_clean_text[verse_id])
                           for score, verse_id in verse_scores[:max_out_length]]

    return most_similar_verses
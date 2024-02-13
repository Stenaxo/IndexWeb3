import math

def bm25(doc_length, avg_doc_length, term_frequency, num_docs, doc_frequency, k1=1.5, b=0.75):
    idf = math.log((num_docs - doc_frequency + 0.5) / (doc_frequency + 0.5) + 1)
    tf_component = term_frequency * (k1 + 1) / (term_frequency + k1 * (1 - b + b * (doc_length / avg_doc_length)))
    return idf * tf_component

  
def rank_documents(doc_ids, content_index, title_index, docs, query_tokens):
    # Convertissez doc_ids en int si ce sont des strings pour correspondre aux indices de la liste docs
    doc_ids_int = [int(doc_id) for doc_id in doc_ids]
    doc_lengths = [len(doc['content']) for doc in docs if doc['id'] in doc_ids_int]
    avg_doc_length = sum(doc_lengths) / len(doc_lengths) if doc_lengths else 0
    num_docs = len(docs)
    scores = {}
    for doc_id in doc_ids_int:
        doc = next((doc for doc in docs if doc['id'] == doc_id), None)
        if not doc:
            continue
        score = 0
        doc_length = len(doc['content'])
        for token in query_tokens:
            term_frequency = 0
            doc_frequency = 0
            if token in content_index:
                term_frequency += sum(content_index[token].get(str(doc_id), {}).get('count', 0) for doc_id in doc_ids_int)
                doc_frequency += len(content_index[token])
            if token in title_index:
                term_frequency += sum(title_index[token].get(str(doc_id), {}).get('count', 0) for doc_id in doc_ids_int)
                doc_frequency += len(title_index[token])
            score += bm25(doc_length, avg_doc_length, term_frequency, num_docs, doc_frequency)
        scores[doc_id] = score
    ranked_doc_ids = sorted(doc_ids_int, key=lambda x: scores.get(x, 0), reverse=True)
    return [str(doc_id) for doc_id in ranked_doc_ids]  # Convertir les ids en strings si nécessaire


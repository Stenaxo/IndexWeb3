from crawler_data_reader import read_documents, read_content_pos_index, read_title_pos_index
from preprocessing import tokenize
from filtering import filter_documents
from ranking import rank_documents
from file_writer import write_to_file

def main():
    docs = read_documents()
    content_index = read_content_pos_index()
    title_index = read_title_pos_index()
    
    query = input("Entrez votre requête: ")
    query_tokens = tokenize(query)
    
    filter_type = input("Choisissez le type de filtre (AND/OR): ").upper()
    if filter_type not in ["AND", "OR"]:
        print("Type de filtre non reconnu, utilisation du filtre AND par défaut.")
        filter_type = "AND"
        
    filtered_doc_ids = filter_documents(query_tokens, content_index, title_index, filter_type)
    
    # Assurez-vous que les fonctions rank_documents et autres prennent en compte les changements nécessaires
    ranked_doc_ids = rank_documents(filtered_doc_ids, content_index, title_index, docs, query_tokens)
    
    # Générer les résultats basés sur les IDs de documents classés
    results = [{'title': docs[int(doc_id)]['title'], 'url': docs[int(doc_id)]['url']} for doc_id in ranked_doc_ids]

    write_to_file('results.json', results)
    
    print(f"Documents initiaux: {len(docs)}, Documents filtrés: {len(filtered_doc_ids)}, Documents après ranking: {len(ranked_doc_ids)}")

if __name__ == "__main__":
    main()

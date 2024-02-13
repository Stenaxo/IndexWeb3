def filter_documents(query_tokens, content_index, title_index, filter_type="AND"):
    filtered_docs = set()
    if filter_type == "AND":
        for token in query_tokens:
            if filtered_docs == set():
                filtered_docs = set(content_index.get(token, {}).keys()) | set(title_index.get(token, {}).keys())
            else:
                filtered_docs &= set(content_index.get(token, {}).keys()) | set(title_index.get(token, {}).keys())
    else:  # "OR"
        for token in query_tokens:
            filtered_docs |= set(content_index.get(token, {}).keys()) | set(title_index.get(token, {}).keys())
    return list(filtered_docs)

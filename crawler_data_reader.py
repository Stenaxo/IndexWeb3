import json

def read_json_file(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def read_documents():
    return read_json_file('documents.json')

def read_content_pos_index():
    return read_json_file('content_pos_index.json')

def read_title_pos_index():
    return read_json_file('title_pos_index.json')

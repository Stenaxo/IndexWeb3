import json

def write_to_file(filename, data):
    """Écrit des données dans un fichier JSON.
    
    Args:
        filename (str): Le chemin du fichier où sauvegarder les données.
        data (dict ou list): Les données à sauvegarder.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

import json
import re

def extract_names(text):
    # Regular expression pattern to find names
    name_pattern = r'\b[A-Z][a-z]+\b'
    names = re.findall(name_pattern, text)
    return names

def process_json(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
        text = data.get('text', '')
        names = extract_names(text)
        return names

if __name__ == "__main__":
    json_file_path = 'your_json_file.json'  # Replace 'your_json_file.json' with the path to your JSON file
    names = process_json(json_file_path)
    print("Names extracted from JSON text:", names)

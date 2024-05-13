# cv_generator.py

def read_template(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError("File not found. Please provide a valid file path.")

def parse_template(template):
    language_parts = [part.strip("{}") for part in template.split("{") if "}" in part]
    stripped_template = template.format(*["" for _ in language_parts])
    return stripped_template, tuple(language_parts)

def merge(template, user_inputs):
    return template.format(*user_inputs)

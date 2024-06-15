import string
from collections import Counter
from ebooklib import epub
from text_analyzer import analyze_text

def extract_text_from_epub(filename):
    try:
        book = epub.read_epub(filename)
        text = ''

        for item in book.get_items():
            if item.get_type() == epub.EpubHtml:
                text += item.get_body_content().decode('utf-8', 'ignore')

        return text

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except Exception as e:
        print(f"Error parsing EPUB file: {e}")
        return None

def analyze_epub_file(filename):
    if filename.endswith('.epub'):
        text = extract_text_from_epub(filename)
        if text:
            analyze_text(text)
    else:
        pass 
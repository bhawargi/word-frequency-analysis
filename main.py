import sys
from epub_handler import analyze_epub_file
from text_analyzer import analyze_text_file, export_to_csv

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <file_name>")
        return
    
    filename = sys.argv[1]
    text_freq = analyze_text_file(filename)
    if text_freq:
        export_to_csv(text_freq, filename)
        analyze_epub_file(filename)

if __name__ == "__main__":
    main()
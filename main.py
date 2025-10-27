import sys

from stats import get_word_count
from stats import count_characters
from stats import report_character_counts

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = str(sys.argv[1])
    book = get_book_text(book_path)
    book_word_count = get_word_count(book)
    book_character_counts = report_character_counts(count_characters(book))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count} total words")
    print("--------- Character Count -------")
    for count in book_character_counts:
        print(f"{count["char"]}: {count["num"]}")
    

main()
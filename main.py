from stats import get_word_count
from stats import count_characters
from stats import report_character_counts

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def main():
    frankenstein_path = "books/frankenstein.txt"
    frankenstein = get_book_text(frankenstein_path)
    word_count_frankenstein = get_word_count(frankenstein)
    character_counts_frankenstein = report_character_counts(count_characters(frankenstein))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {frankenstein_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count_frankenstein} total words")
    print("--------- Character Count -------")
    for count in character_counts_frankenstein:
        print(f"{count["char"]}: {count["num"]}")
    

main()
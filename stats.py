def get_word_count(book_text):
    return len(book_text.split())

def count_characters(book_text):
    character_counts = {}
    for character in book_text.lower():
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1
    
    return character_counts

def report_character_counts(character_counts):
    def sort_on(items):
        return items["num"]
    
    list_of_character_counts = []
    for character, count in character_counts.items():
        if character.isalpha():
            character_dictionary = {"char": character, "num": count}
            list_of_character_counts.append(character_dictionary)

    list_of_character_counts.sort(reverse=True, key=sort_on)
    return list_of_character_counts
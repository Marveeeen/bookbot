import sys
from stats import *


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = f"./{sys.argv[1]}"
    book_text =get_book_text(file_path)
    num_words = get_num_words(book_text)
    num_word_dict =  get_num_word_dict(book_text)
    character_list = get_list_of_characters(num_word_dict)
    sorted_character_list = sort_character_list(character_list)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for character in sorted_character_list:
        print(f"{character['char']}: {character['num']}")


if __name__ == "__main__":
    main()
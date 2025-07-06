def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(text):
    return len(text.split())

def get_char_dict(text):
    text_set = set(text.lower())
    return dict((char, text.count(char)) for char in text_set)

def sort_on(items):
    return items["num"]

def sort_char_list(text_dict):
    text_dict.sort(reverse=True, key=sort_on)
    return text_dict

def get_char_list(book_text):
    text_dict = get_char_dict(book_text)
    char_list = [{"char": char, "num": num} for char, num in text_dict.items() if char.isalpha()]

    return sort_char_list(char_list)


    
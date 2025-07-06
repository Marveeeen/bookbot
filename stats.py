def get_num_words(text):
    text = text.split()
    return len(text)

def get_num_word_dict(text):
    text = text.lower().split()
    text = "".join(text)
    text_dict = {}

    for word in text:
        if word in text_dict:
            text_dict[word] += 1
        else:
            text_dict[word] = 1
    
    return text_dict

def get_list_of_characters(text_dict):
    character_list = []
    for word, count in text_dict.items():
        character_list.append({"char": word, "num": count})
        

    return character_list

def sort_on(items):
    return items["num"]

def sort_character_list(text_dict):
    text_dict.sort(reverse=True, key=sort_on)
    return text_dict

    
def count_words(text):
    words = text.split()
    num_words = len(words)
    print(f"Found {num_words} total words")

def count_chars(text):
    dict = {}
    text = text.lower()
    for character in text:
        if character not in dict:
            dict[character] = 1
        else:
            dict[character] += 1
    return dict

def dict_num(dict):
    return dict["num"]


def sort_dict(dict):
    new_list = []
    char_count = count_chars(dict)
    for i in char_count:
        new_dict = {}
        new_dict["char"] = i
        new_dict["num"] = char_count[i]
        new_list.append(new_dict)
    new_list.sort(reverse=True, key=dict_num)
    return new_list

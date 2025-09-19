def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def count_words(path):
    text = get_book_text(path)
    words = text.split()
    return f'{len(words)} words found in the document'

def count_characters(path):
    """
    The objective of this function is to display every single character in a string
    and the number of times it appears

    Args:
        path(str): path to the txt files that contains the text
    Returns:
        Dict: it returns a dictionary with the character as key and number of times as value
    """
    text = get_book_text(path)
    res = dict()
    for char in text.lower():
        if char == " ":
            continue
        if not char.isalpha():
            continue
        if char in res:
            res[char] += 1
        else:
            res[char] = 1

    return res

def list_of_dictionaries(dictio):
    """
    Get a dictionary and breaks the keys into a list of dictionaries
    Args:
        dictio(dict): A dictionary with the number of character
    Returns:
        A list of dictionaries
    """
    lista = []
    for key,value in dictio.items():
        new_dict = {}
        new_dict["char"] = key
        new_dict['num'] = value
        lista.append(new_dict)
    
    return lista


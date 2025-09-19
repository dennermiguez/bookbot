from stats import count_words, count_characters, list_of_dictionaries
import sys

if len(sys.argv) != 2:
    "Usage: python3 main.py <path_to_book>"
    sys.exit(1)


caminho = sys.argv[1]

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def sort_on(items):
    return items["num"]

palavras = count_words(caminho)

dict_char = count_characters(caminho)

lista_dict = list_of_dictionaries(dict_char)

lista_dict.sort(reverse=True, key=sort_on)

# Impressão automática
print("="*30)
print("BOOKBOT".center(30))
print("="*30)
print(f"Analyzing book found at {caminho}...")
print("-"*30)
print("Word Count".center(30))
print("-"*30)
print(palavras)
print("-"*30)
print("Character Count".center(30))
print("-"*30)
for i in lista_dict:
    print(f'{i["char"]} : {i["num"]}')

print("="*30)
print("END")
print("="*30)







    
 


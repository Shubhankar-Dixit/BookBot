import sys
from stats import get_num_words, character_count, chars_dict_to_sorted_list

if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    file_path = sys.argv[1]

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def print_report(file_path, word_count, sorted_chars_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path} ---")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for item in sorted_chars_list:
        print(f"{item['char']}: {item['num']}")
        
    print("============= END =============")

def main():
    text = get_book_text(file_path)
    word_count = get_num_words(text)
    sorted_chars_list = chars_dict_to_sorted_list(character_count(text))
    print_report(file_path, word_count, sorted_chars_list)

main()
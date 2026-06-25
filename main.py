from stats import get_num_words, character_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_path = 'books/frankenstein.txt'
    text = get_book_text(file_path)

    word_count = f"Found {get_num_words(text)} total words"
    print(word_count)
    character_count(text)

main()

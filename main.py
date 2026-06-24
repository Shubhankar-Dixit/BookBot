from stats import get_book_word_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    word_count = f"Found {get_book_word_count('books/frankenstein.txt')} total words"
    print(word_count)

main()

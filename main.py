def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def get_book_word_count(file_path):
    with open(file_path) as f:
        # You need to read the file before you split it
        raw_text = f.read().split()
    return len(raw_text)

def main():
    word_count = f"Found {get_book_word_count("books/frankenstein.txt")} words total"
    print(word_count)

main()

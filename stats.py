def get_book_word_count(file_path):
    with open(file_path) as f:
        # You need to read the file before you split it
        raw_text = f.read().split()
    return len(raw_text)
def get_num_words(file_path):
    with open(file_path) as f:
        raw_text = f.read().split()
    return len(raw_text)

def character_count(file_path):
    char_dict = {}
    
    with open(file_path) as f:
        text = f.read().lower()
        char_list = list(text)
        
        for char in char_list:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
                
    for char in char_dict:
        count = char_dict[char]
        print(f"'{char}': {count}")

def get_num_words(file_contents):

    raw_text = file_contents.split()
    return len(raw_text)

def character_count(file_contents):
    char_dict = {}

    text = file_contents.lower()
    char_list = list(text)  
        
    for char in char_list:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
                
    for char in char_dict:
        count = char_dict[char]
        print(f"'{char}': {count}")

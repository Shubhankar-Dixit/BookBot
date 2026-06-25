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
                
    return char_dict

def sort_on(unsorted_list):
    sorted_list = sorted(unsorted_list, reverse=True)
    return sorted_list

def chars_dict_to_sorted_list(chars_dict):
    chars_list = list(chars_dict.items())
    sorted_chars_list = sort_on(chars_list)
    result = []
    for item in sorted_chars_list:
        result.append({'char': item[0], 'num': item[1]})
    return result
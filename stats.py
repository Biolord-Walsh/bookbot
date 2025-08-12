#counts words in file
def count_words(filepath):
    return len(filepath.split())

#creates dictionary and counts number of characters
def char_count(text):
    chars = {}
    for character in text.lower():
        if character in chars:
            chars[character] += 1
        else:
            chars[character] = 1
    return chars

def sort_on(char):
    return char["num"]

def sort_chars(char_count_dict):
    char_list = []
    for char, num in char_count_dict.items():
        char_list.append({"char": char, "num": num})
    char_list.sort(reverse=True, key=sort_on) # Sorts the list in place
    return char_list # Returns the now-sorted list
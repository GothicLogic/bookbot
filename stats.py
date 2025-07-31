def count_words(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    print(f"Found {count} total words")

def count_chars(text):
    char_count= {}
    lower_text = text.lower()
    for letter in lower_text:
        if letter not in char_count:
            char_count[letter] = 0
        char_count[letter] += 1
    return char_count

def sort_dict(char_dict):
    char_list = []
    for char in char_dict:
        count = char_dict[char]
        sorted_dict = {"char": char, "count": count}
        char_list.append(sorted_dict)
    char_list.sort(reverse = True, key = sort_on)
    for dict in char_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["count"]}")

def sort_on(char_dict):
    return char_dict["count"]
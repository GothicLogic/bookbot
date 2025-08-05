def count_words(text):
    count = 0
    words = text.split() # Split the text into a list of words

    for word in words:
        count += 1 # Increment count for each word

    print(f"Found {count} total words")

def count_chars(text):
    char_count= {} # Dictionary to store character counts
    lower_text = text.lower() # Convert text to lowercase for uniform counting

    for letter in lower_text:
        if letter not in char_count:
            char_count[letter] = 0  # Initialize count for new character
        char_count[letter] += 1 # Increment count for character

    return char_count # Return the dictionary of character counts

def sort_dict(char_dict):
    char_list = [] # List to hold dictionaries of characters and their counts

    for char in char_dict:
        count = char_dict[char]
        sorted_dict = {"char": char, "count": count} # Create dict for each character
        char_list.append(sorted_dict) # Add to the list

    # Sort the list of dicts in descending order by count
    char_list.sort(reverse = True, key = sort_on) 

    # Print only alphabetical characters and their counts
    for dict in char_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["count"]}")

def sort_on(char_dict):
    return char_dict["count"]  # Helper function to get the count for sorting
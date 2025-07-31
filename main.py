from stats import count_words
from stats import count_chars
from stats import sort_dict
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
     if len(sys.argv) < 2:
         print("Usage: python3 main.py <path_to_book>")
         sys.exit(1)
         
     path = sys.argv[1]
     text = get_book_text(path)

     print("============ BOOKBOT ============")
     print(f"Analyzing book found at {path}")
     print("----------- Word Count ----------")
     count_words(text)
     print("--------- Character Count -------")
     char_dict = count_chars(text)
     sort_dict(char_dict)
     print("============= END ===============")

main()
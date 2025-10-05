from stats import *
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    sorted_list = sort_dict(get_book_text(sys.argv[1]))
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------")
    count_words(get_book_text(sys.argv[1]))
    print("--------- Character Count -------")
    for i in sorted_list:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

main()
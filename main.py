from stats import word_count
from stats import characters
from stats import get_book_text
from stats import sorted_dictionary
import sys

   
def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_link = sys.argv[1]
    text = get_book_text(book_link)
    w_count = word_count(text)
    character_count = characters(text)
    sorted = sorted_dictionary(character_count)

    print("============ BOOKBOT ===============")
    print(f"Analyzing book found at {book_link}")
    print("------------ Word Count ------------")
    print(f"Found {w_count} total words")
    print("--------- Character Count ----------")

    for sort in sorted:
        print(f"{sort['char']}: {sort['num']}")
    
    print("============== END =================")




main()
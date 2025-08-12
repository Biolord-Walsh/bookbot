import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    bookpath = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


from stats import count_words, char_count, sort_chars


def main():
    book_content = get_book_text(bookpath)
    wordcount = count_words(book_content)
    num_char = char_count(book_content)
    sort_char = sort_chars(num_char)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    for dict in sort_char:
        char = dict["char"]
        if not char.isalpha():
            continue
        print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")

main()
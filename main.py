# Take a filepath as input and return the contents of the file as a string
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

#runs functions in stats
from stats import count_words

#defines path, prints word count
def main():
    book_content = get_book_text("./books/frankenstein.txt")
    print(f"{count_words(book_content)} words found in the document")

main()
# Take a filepath as input and return the contents of the file as a string
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

# CH2 Lesson 2 Assignment Part 3 function.
# Instructions: (Use) get_book_text with the relative path to your frankenstein.txt file to print 
# the entire contents of the book to the console.
def main():
    book_content = get_book_text("./books/frankenstein.txt")
    print(book_content)

main()
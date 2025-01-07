from collections import Counter


def main():
    book_path ="books/frankenstein.txt"
    full_text = get_text(book_path)
    num_words = count_words(full_text)
    num_letters = count_letters(full_text)
    print(num_words)
    print(num_letters)

#This counts the number of words in the entire text of a specified file or book
def count_words(text):
    words = text.split()
    words_number = len(words)
    return words_number

#This extracts all the text from a specified file and returns it. Used in the main and stores the text as a string variable.
def get_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()


#This lowers the case of all upper case letters so we don't have any upper case, and allows us to have no duplicate, then it counts the amount of letters
def count_letters(text):
    no_caps = text.lower()
    count = Counter(no_caps)
    return count

#This will output a consice repport with every

main()

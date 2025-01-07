def main():
    book_path ="books/frankenstein.txt"
    full_text = get_text(book_path)
    num_words = count_words(full_text)
    print(num_words)

def count_words(text):
    words = text.split()
    words_number = len(words)
    return words_number
    
def get_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()

main()

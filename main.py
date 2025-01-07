from collections import Counter

def main():
    book_path ="books/frankenstein.txt"
    full_text = get_text(book_path)
    num_words = count_words(full_text)
    num_letters = count_letters(full_text)
    char_list = convert_to_list(num_letters)
    print(num_words, "words found in the document")
    print(num_letters)
    char_list.sort(reverse=True, key=sort_on)
    print(char_list)

#This counts the number of words in the entire text of a specified file or book
def count_words(text):
    words = text.split()
    words_number = len(words)
    return words_number

#This extracts all the text from a specified file and returns it. Used in the main and stores the text as a string variable.
def get_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()


#This lowers the case of all upper case letters so we don't have any upper case, and allows us to have no duplicate, then it counts the amount of characters
def count_letters(text):
    no_caps = text.lower()

    #Remove non alphabetic characters - Keep letters only
    letters_only = [char for char in no_caps if char.isalpha()]
    # Same thing written out:
    # letters_only = []
    # for char in no_caps:
    #     if char.isalpha():
    #         letters_only.append(char)


    #Then count
    count = Counter(letters_only)
    return count


#This will turn the counter list into a list of dictionnaries to make a report
def convert_to_list(counter_dict):
    char_list = []
    for letter, count in counter_dict.items():
        char_dict = {"letter": letter, "count": count}
        char_list.append(char_dict)
    return char_list #Here, True means that you go in descending order, from highest to lowest


#This will tell the sort function, which data to use to sort the dict
def sort_on(dict):
    return dict["count"]



main()

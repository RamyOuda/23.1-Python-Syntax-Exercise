def print_upper_words(list, letter):
    """Converts all strings in an array to uppercase"""

    for each in list:
        if each[0].upper() == letter.upper():
            print(each.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes", "eagle"], "h")

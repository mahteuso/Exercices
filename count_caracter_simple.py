def count_character(s):
    """
    Using Dictionary
    """
    dic_letters = {}
    
    for letter in sorted(s):
        dic_letters[letter] = dic_letters.get(letter, 0) + 1
    print(dic_letters)
    
    


if __name__ == '__main__':
    count_character('banana')

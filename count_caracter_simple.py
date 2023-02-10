def count_character(s):
    """
    Using Dictionary
    """
    dic_letters = {}
    
    for letter in sorted(s):
        dic_letters[letter] = dic_letters.get(letter, 0) + 1
    print(dic_letters)
    
    """Using list
    ordened_words = sorted(s)
    previus_letter = ordened_words[0]
    count = 1

    for letter in ordened_words[1:]:
        if letter == previus_letter:
            count += 1
        else:
            print(f"{previus_letter}: {count}")
            previus_letter = letter
            count = 1
    print(f"{letter}: {count}")
    """
    


if __name__ == '__main__':
    count_character('banana')

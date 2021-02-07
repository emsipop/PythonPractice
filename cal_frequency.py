def cal_frequency():

    # The input string is provided by the user
    string = str(input("Enter a string: "))

    # All characters will be in lowercase
    sentence = string.lower()

    # Removes whitespace from the input string
    sentence = sentence.replace(" ", "")

    # Removes all characters except the letters of the alphabet from the input string
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    sentence = filter(alphabet.__contains__, sentence)

    # Empty dictionary created to store the letters used and their frequency
    letter_freq = {}

    # For each letter in the string, each time the letter occurs again 1 is added to it's total number of occurances
    for letter in sentence:
        if letter in letter_freq:
            letter_freq[letter] += 1
        else:
            letter_freq[letter] = 1 # Otherwise, if only found once in the string the number of occurances will be set to 1

    # Each of the keys (letters) and values (frequencies) stored in the dictionary are be printed
    for keys, values in sorted(letter_freq.items(), key = lambda item: item[1], reverse = True): # The dictionary is rearranged by value in descending order
        print(keys, "was used this many times:", values)

    print("No other letters in the alphabet have been used.")
def pig_latin():
    string = input("Please enter a string you would like translating: ").lower() #Changes case of all characters to lower
    words = string.split(" ") # Splitting the user's input into an array, each item corresponding to each word in the sentence
    translation = [] # An empty array which each translated word will be appended to

    for word in words: # The following will occur for each item in the array
        translation.append(word[1:] + word[0] + "ay") # Each word is translated and added to the new array

    return " ".join(translation) # The new array is then turned back into a string and is returned to give the full translated string

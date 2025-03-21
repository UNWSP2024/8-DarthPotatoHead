#Program Written By: Ainsley Bellamy
#Date Written: 03/21/2025
#Program Title: Word_Separator


# Program #2: Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together, 
# but the first character of each word is uppercase.  
# Convert the sentence to a string in which the words are separated by spaces, 
# and the first word starts with an uppercase.  
# For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."

# Start your changes on line 13

def word_separator(sentence):
    new_sentence = ""
#First, strip sentence to remove unnecessary white space.
    sentence = sentence.strip()
#First add the first character of the string the user inputted, making sure it is uppercase.
    new_sentence += sentence[0].upper()
#Next, loop through all character except the first to check for uppercase letters.
    for char in sentence[1:len(sentence)]:
#If a letter is uppercase, first add a space to the new_sentence variable then
# add that character in lowercase.
        if char.isupper():
            new_sentence += ' '
        new_sentence += char.lower()
#Finally, add a period cause it looks nice.
    if sentence[-1] != '.':
        new_sentence += '.'
    return new_sentence

#Main function gets user input, runs above function, and prints results.
def main():
    sentence = str(input("Enter a sentence in which all the words to strung together and capitalized: "))
    new_sentence = word_separator(sentence)
    print(new_sentence)

if __name__ == "__main__":
    main()
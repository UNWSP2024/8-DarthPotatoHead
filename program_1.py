#Program Written By: Ainsley Bellamy
#Date Written: 03/21/2025
#Program Title: Get_Initials


# Program #1: Initials
# Write a program that gets a string containing a person's first, middle, and last names, 
# and displays their first, middle, and last initials.  
# For example, if the user enters John William Smith, the program should display J. W. S.

# Add your logic starting on line 11

def initials_generator(personsName):
    personsInitials = ""
#Split user input on spaces to work with each separate name.
    fullName = personsName.split()
#Loop through each name, take the first character, make it uppercase and add a period
#plus a space and add it to personsInitials variable.
    for name in fullName:
        personsInitials += name[0].upper() + '. '
    return personsInitials.strip()

#Get the users full name and call above function, then print.
def main():
    personsName = input('Enter the users first, middle, and last name separated by spaces: ')
    initials = initials_generator(personsName)
    print(initials)

#Call main function.
if __name__ == "__main__":
    main()
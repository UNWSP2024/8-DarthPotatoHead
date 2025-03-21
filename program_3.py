#Program Written By: Ainsley Bellamy
#Date Written: 03/21/2025
#Program Title: Capital_Quiz


# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values.  
# The program should then randomly quiz the user by displaying the name of a state 
# and asking the user to enter the state's capital.  
# The program should count of the number of correct and incorrect responses.  
# (You could alternatively use another country and provinces, 
# or countries of the world and capitals).
import random

#Function to actually give the quiz.
def capitalQuiz():
    stateCapitals = {
        "Alabama" : "montgomery",
        'Alaska' : 'juneau',
        'Arizona' : 'phoenix',
        'Arkansas' : 'little rock',
        'California' : 'sacramento',
        'Colorado' : 'denver',
        'Connecticut' : 'hartford',
        'Delaware' : 'dover',
        'Florida' : 'tallahassee',
        'Georgia' : 'atlanta',
        'Hawaii' : 'honolulu',
        'Idaho' : 'boise',
        'Illinois' : 'springfield',
        'Indiana' : 'indianapolis',
        'Iowa' : 'des moines',
        'Kansas' : 'topeka',
        'Kentucky' : 'frankfort',
        'Louisiana' : 'baton Rouge',
        'Maine' : 'augusta',
        'Maryland' : 'annapolis',
        'Massachusetts' : 'boston',
        'Michigan' : 'lansing',
        'Minnesota' : 'saint paul',
        'Mississippi' : 'jackson',
        'Missouri' : 'jefferson city',
        'Montana' : 'helena',
        'Nebraska' : 'lincoln',
        'Nevada' : 'carson city',
        'New Hampshire' : 'concord',
        'New Jersey' : 'trenton',
        'New Mexico' : 'santa Fe',
        'New York' : 'albany',
        'North Carolina' : 'raleigh',
        'North Dakota' : 'bismarck',
        'Ohio' : 'columbus',
        'Oklahoma' : 'oklahoma city',
        'Oregon' : 'salem',
        'Pennsylvania' : 'harrisburg',
        'Rhode Island' : 'providence',
        'South Carolina' : 'columbia',
        'South Dakota' : 'pierre',
        'Tennessee' : 'nashville',
        'Texas' : 'austin',
        'Utah' : 'salt lake city',
        'Vermont' : 'montpelier',
        'Virginia' : 'richmond',
        'Washington' : 'olympia',
        'West Virginia' : 'charleston',
        'Wisconsin' : 'madison',
        'Wyoming' : 'cheyenne'
    }
#Scorekeeper which will be summed at the end.
    score = []
#While loop preset condition.
    keep_going = 'y'
    while keep_going.lower() == 'y':
#Chooses a random key to display to the user.
        rando = random.choice(list(stateCapitals.keys()))
        answer = str(input(f'Enter the capital of {rando}: '))
#Checks key against its value and appends either 1 or 0 according to whether the user answer right or wrong.
        if answer.lower() == stateCapitals[rando]:
            print("That's right!")
            score.append(1)
        else:
            print("Wrong!")
            score.append(0)
#Ask the user if they want to continue.
        keep_going = str(input("Would you like to answer another? Press 'y' to continue: "))
#Return score.
    return (sum(score) / len(score)) * 100

#Main function to call above function and display score.
def main():
    print(f"Score: {capitalQuiz():.2f}%")

if __name__ == "__main__":
    main()
#Program Written By: Ainsley Bellamy
#Date Written: 03/21/2025
#Program Title: CourseDisplay


# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.

#Define function to get course/name pairs from user.
def getCourses():
#Pairs will be added to dictionary.
    CourseNamePairs = {}
#Controls the while loop.
    keep_going = 'y'
    while keep_going.lower() == 'y':
#Get key (course) and use that to add a key/value pair to the dictionary.
        courseID = str(input("Enter a course ID (Example: COS 2005): "))
        CourseNamePairs[courseID] = str(input("Enter the course name (Example: Computer Science): "))
        keep_going = str(input("Would you like to enter another Course/Name pair? (y/n): "))
    return CourseNamePairs

#Function to allow the user to search their inputted course/name pairs.
def getSubject(subjects):
    subject = str(input("Enter a search term: "))
    print("Here are the courses that match that term:")
#Checks each key against the user's input and displays all courses that match. Else, nothing.
    for courseCode in subjects:
        if subject in courseCode:
            print(f"{courseCode}, {subjects[courseCode]}")
        else:
            print("Subject not found.")

#Call above functions.
def main():
    getSubject(getCourses())

if __name__ == "__main__":
    main()
#Creating dictionaries for the course details
classNumber = {
    'CSC101': '3004',
    'CSC102': '4501',
    'CSC103': '6755',
    'NET110': '1244',
    'COM241': '1411'
}

instructorName = {
    'CSC101': 'Haynes',
    'CSC102': 'Alvarado',
    'CSC103': 'Rich',
    'NET110': 'Burke',
    'COM241': 'Lee'
}

meetingTimes = {
    'CSC101': '8:00 a.m.',
    'CSC102': '9:00 a.m.',
    'CSC103': '10:00 a.m.',
    'NET110': '11:00 a.m.',
    'COM241': '1:00 p.m.'
}

#Getting user input
courseNumber = input("Enter a course number: ")

# Display course details
if courseNumber in classNumber:
    print(f"Course Number: {courseNumber}")
    print(f"Room Number: {classNumber[courseNumber]}")
    print(f"Instructor: {instructorName[courseNumber]}")
    print(f"Meeting Time: {meetingTimes[courseNumber]}")
else:
    print("Course number not found.")

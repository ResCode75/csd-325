# Rachel Shaw - 8.2 Assignment - 12/6/24

import json

# load json file as a python list
with open('student.json') as f:
    ClassList = json.load(f)

# print student list
def display_students():
    index = 0
    for i in ClassList:
        student = ClassList[index]
        print(f'{student['F_Name']} {student["L_Name"]}: ID= {student["Student_ID"]}, Email= {student["Email"]}')
        index += 1

# add myself to the student list
def add_me():
    me = {
    "F_Name": "Rachel",
    "L_Name": "Shaw",
    "Student_ID": "12707",
    "Email": "rshaw@gmail.com"
    }

    ClassList.append(me)
    
    #notify user that list has been updated
    print("\n--CLASS LIST UPDATED-- \n")

# dump updated list to json file
def update_json():
    with open('student.json', 'w') as f:
        json.dump(ClassList, f, indent=4)
    
    #notify users that the json file has been updated
    print("\n--JSON FILE UPDATED--")
    

def main():

    #notify user that this is the original list 
    print("\nORIGINAL LIST:")

    display_students()

    add_me()
    
    #notify users that this is the updated list
    print("UPDATED LIST:")

    display_students()

    update_json()
    

main()
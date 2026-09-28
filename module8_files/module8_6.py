#Problem 6

students = 0
question = input("Do you want to do this program? ")
if question in ("Yes", "yes"):
    pass
else:
    quit()
while question in ("Yes", "yes"):
    last_name = input("Please enter your last name: ")
    exam_one = float(input("Enter exam one score: "))
    exam_two = float(input("Enter exam two score: "))
    exam_average = (exam_one + exam_two)/2
    students += 1
    print(f"Last name: {last_name} Exam Average: {exam_average:.1f}%")
    next_student = input("Would you like to continue this program? ")
    if next_student in ("Yes", "yes"):
        pass
    else:
        break
print(f"Total number of students: {students}")
    

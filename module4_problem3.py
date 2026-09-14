#Python 3.14.7 (v3.14.7:823f0323ee6, Aug  5 2026, 07:07:01) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
#Enter "help" below or click "Help" above for more information.


###Problem 3 in Module 3/4 Assignment
#The student will enter their last name, midterm and final exam scores (0 – 100
#points). Compute the total exam points to be the sum of 40% of midterm and
#60% of the final exam. Display student last name and total exam points.
                      

#variables for last name, midterm and final exam scores

last_name = input("Enter the student's last name: ")
midterm_score = float(input("Enter midterm points: "))
finalexam_score = float(input("Enter final exam points: "))

#calculate total exam point - .4 midterm and .6 final exam
studentexam_total = (midterm_score * .4) + (finalexam_score *.6)
#ouptut is last name and total exam points

print("Student Total Exam Points")
print(f"{last_name}: %{studentexam_total:.1f}")

#problem 5


name_line = 0
district_line = 1
credit_line = 2
i_cost = float(250)
o_cost = float(500)
tuition_sum = float(0)
student_sum = float(0)
with open('student_tuition.txt', 'r') as d:
    d_contents = d.readlines()
    d_length = len(d_contents)
    while name_line < d_length:
        name = d_contents[name_line].strip()
        district = d_contents[district_line].strip()
        credit = float(d_contents[credit_line].strip())
        name_line += 3
        district_line += 3
        credit_line += 3
        credit_cost = float(250 if district == "I" else 500)
        tuition_owed = credit * credit_cost
        tuition_sum += tuition_owed
        student_sum += 1
        if name == "":
            break
        print(f"Student: {name} Credits Taken: {credit:.0f} Tuition Owed: ${tuition_owed:.2f}")
print(f"Sum of All Tuition Owed: ${tuition_sum:.2f}")
print(f"Total Students: {student_sum:.0f}")

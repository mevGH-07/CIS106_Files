#Problem 3

name_line = 0
salary_line = 1
bonus_total = 0
with open('employee_salaries.txt', 'rt') as b:
    b_content = b.readlines()
    b_length = len(b_content)
    while name_line < b_length:
        name = b_content[name_line].strip()
        salary = float(b_content[salary_line].strip())
        bonus_percent = float(.2 if salary >= 100000 else .15 if salary == 50000 else .1)
        bonus_amount = salary * bonus_percent
        name_line += 2
        salary_line += 2
        bonus_total += bonus_amount
        if name == "":
            break
        print(f"Employee: {name}, Salary: ${salary:.2f}, Bonus: ${bonus_amount:.2f}")
print(f"Total Bonus: ${bonus_total:.2f}")



    

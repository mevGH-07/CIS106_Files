

#Problem 6
#The user will enter employee last name, salary and job level (as noted
#below). Use the job level to determine the bonus rate. Then compute
#bonus to be salary times bonus rate. Display employee last name and
#bonus.
#Job Level Bonus Rate
#10 and above 25%
#5 to 9 20%
#All others 10%

last_name = input("Please enter employee last name: ")
salary = float(input("Please enter employee salary: "))
job_level = input("Please enter job level: ")

bonus_rate = float(.25 if job_level >= "10"
                      else .2 if (ticket_number >= "5" and ticket_number <= "9")
                      else .1)
bonus_converted = bonus_rate * 100
bonus_total = salary * bonus_rate

print(f"Employee Last Name: {last_name}")
print(f"Bonus Amount: ${bonus_total:.2f}")


                   

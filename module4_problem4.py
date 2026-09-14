#Python 3.14.7 (v3.14.7:823f0323ee6, Aug  5 2026, 07:07:01) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
#Enter "help" below or click "Help" above for more information.



### Problem 4 in Module3/4 Assignment
#You and two friends completed a job and received an amount that is entered into
#the problem. You are to split the amount received evenly between the three of
#you. Compute and display what each of you will receive.

##variables for amount in job and split in job

total_amount = float(input("Total amount paid for task: "))

split_amount = total_amount/3

print(f"Each person will be paid: ${split_amount:.2f}")


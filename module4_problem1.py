#Python 3.14.7 (v3.14.7:823f0323ee6, Aug  5 2026, 07:07:01) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
#Enter "help" below or click "Help" above for more information.


###Problem 1 in Module 3/4 Assignment
exam_one = input("Enter first exam scores: ")
exam_two = input("Enter second exam scores: ")

float_one = float(exam_one)
float_two = float(exam_two)

exam_total = (float_one * .6) + (float_two * .4)
examtxt = f"Exam Total: {exam_total:.1f}%"

print(examtxt)



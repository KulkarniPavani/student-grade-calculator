# Student Grade Calculator

name = input("Enter student name: ")

sub1 = int(input("Enter marks for Subject 1: "))
sub2 = int(input("Enter marks for Subject 2: "))
sub3 = int(input("Enter marks for Subject 3: "))

total = sub1 + sub2 + sub3
average = total / 3

print("\n----- Result -----")
print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks:", average)

if average >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")

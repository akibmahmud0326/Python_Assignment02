name = input("Enter student name: ")
sub1 = int(input("Marks in Subject 1: "))
sub2 = int(input("Marks in Subject 2: "))
sub3 = int(input("Marks in Subject 3: "))

total = sub1 + sub2 + sub3
average = total / 3
percentage = (total / 300) * 100

if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "F"

passed = sub1 >= 40 and sub2 >= 40 and sub3 >= 40

scholarship = average >= 85 and sub1 >= 80 and sub2 >= 80 and sub3 >= 80

sub1 += 5
sub2 += 5
sub3 += 5

new_total = sub1 + sub2 + sub3
new_average = new_total / 3

print("\n--- Student Report ---")
print("Name: ", name)
print("Total Marks (before bonus): ", total)
print("Average (before bonus): ", average)
print("Percentage: ", percentage)
print("Grade: ", grade)
print("Passed All Subjects: ", passed)
print("Eligible for Scholarship: ", scholarship)
print("Total After Bonus: ", new_total)
print("Average After Bonus: ", new_average)

# Midterm 1: Problem 6
# Henry Rybolt

num_courses = input("How many coursed did you take last semester? ")

courses = [""] * num_courses
grades = [0] * num_courses
running_sum = 0

for i in range(num_courses):
	courses[i] = raw_input("What was the name of one of the coureses? ")
	grades[i] = input("What was your grade in that course? ")
	running_sum = running_sum + grades[i]

average = float(running_sum) / float(num_courses)

print "REPORT CARD:"

for i in range(num_courses):
	print courses[i] ,
	print "-",
	print grades[i]

print "Overall GPA - ",
print average

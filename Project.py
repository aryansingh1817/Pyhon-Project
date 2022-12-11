Names = input("Enter the names of students separated by commas: ").split(",")
Marks = input("Enter the marks of students separated by commas: ").split(",")
Updates = input("Enter the updates separated by commas: ").split(",")

#Converting Marks to int
Marks = [int(x) for x in Marks]

#Updating the marks
for i in range(len(Marks)):
    Marks[i] = Marks[i] + int(Updates[i])

#Finding Maximum Marks
max_marks = max(Marks)

#Finding the name of student with maximum marks
for i in range(len(Marks)):
    if Marks[i] == max_marks:
        print("Name of the student with maximum marks after updation is:",Names[i])

#Finding the jump in the rank
for i in range(len(Marks)):
    if Marks[i] == max_marks:
        prev_rank = i + 1
        break


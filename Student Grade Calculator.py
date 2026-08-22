def calculate_grade(percentage):

    if percentage >= 90:
        return "A", "Excellent! Outstanding work! "

    elif percentage >= 80:
        return "B", "Very Good! Keep it up! "

    elif percentage >= 70:
        return "C", "Good job! Keep improving! "

    elif percentage >= 60:
        return "D", "You passed! Keep working harder! "
    elif percentage >= 35:
        return "PASS", "You passed! But there's room for improvement! "

    else:
        return "F", "Don't give up! You can do better! "


print("🎓 STUDENT GRADE CALCULATOR")

print("----------------------------")

name = input("Enter student name: ")

# Enter marks for 5 subjects
subjects = ["Tamil", "English", "Maths", "Physics", "Computer"]
marks = []

for subject in subjects:

    while True:
        try:
            mark = float(input(f"Enter {subject} mark (0-100): "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print(" Marks must be between 0 and 100.")

        except ValueError:
            print(" Please enter a valid number.")

total = sum(marks)
percentage = (total / 500) * 100
grade, message = calculate_grade(percentage)

print("\n RESULT FOR", name.upper())
print("----------------------------")

for i in range(5):
    print(subjects[i], ":", marks[i])

print("----------------------------")
print("Total:", total, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Message:", message)
grades = ("A", "B", "C", "D", "F")


students = []

for i in range(5):
    print("Student", i + 1)

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    hours = float(input("Enter study hours: "))
    score = float(input("Enter Python score: "))

    student = {
        "name": name,
        "age": age,
        "hours": hours,
        "score": score
    }

    students.append(student)



def average_score():
    total = 0

    for student in students:
        total = total + student["score"]

    return total / len(students)


passing = 0
failing = 0

print(" STUDENT REPORT ")

for student in students:
    score = student["score"]

    if score >= 80:
        grade = grades[0]
    elif score >= 70:
        grade = grades[1]
    elif score >= 60:
        grade = grades[2]
    elif score >= 40:
        grade = grades[3]
    else:
        grade = grades[4]

    if score >= 40:
        result = "Pass"
        passing = passing + 1
    else:
        result = "Fail"
        failing = failing + 1

    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Study Hours:", student["hours"])
    print("Score:", score)
    print("Grade:", grade)
    print("Result:", result)


print("Total students:", len(students))
print("Average score:", round(average_score(), 2))
print("Passing students:", passing)
print("Failing students:", failing)
print("Grade categories:", grades)
def calculate_average(scores):
    if len(scores)==0:
        return 0

    return sum(scores)/len(scores)
marks=[70,80,90] 
result=calculate_average(marks)
print("Average:",result)
print("total",sum)

def classify_score(score):
    if score < 0 or score>100:
        return"Invalid"
    elif score>=80:
        return"Excellent"
    elif score>=60:
        return"Good"
    elif score >=40:
        return"Pass"
    else:
        return"Fail"
    print(classify_score(90))
    print(classify_score(55))
    print(classify_score(25))









scores=[55,80,35,90,65]
scores.append(75)
print(scores)
scores[1]=85
print(scores)
print("Hightest:", max(scores))
print("lowest:",min(scores))
print(sum(scores)/len(scores))

for score in scores:
    if(score>=80):
        print(score)


student={
            "name":"Su Su",
            "age": 20,
            "score":80,
            "passed":True

}
print(student["name"])
print(student["score"])

students =[
    {"name":"Aung Aung","score":85},
    {"name":"Su Su","score":92},
    {"name":"Mg Mg","score":35},

]
for student in students:
    print(student["name"],student["score"])


def student_grade():
    print("student_grade")
student_grade()
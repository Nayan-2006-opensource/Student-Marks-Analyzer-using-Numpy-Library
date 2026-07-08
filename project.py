import numpy as np

marks = np.random.randint(1, 101, 75).reshape(15, 5)

subject = np.array(["Maths", "Physics", "Chemistry", "Biology", "English"])

student = np.array([f"Student {i}" for i in range(1, 16)])

for i in range(len(student)):
    print(f"\n{student[i]}")
    for j in range(len(subject)):
        print(f"{subject[j]} : {marks[i, j]}")


total=marks.sum(axis=1) #total marks of each student
print(total)
for i in range(len(total)):
    print("total marks of student",student[i],"is",total[i])
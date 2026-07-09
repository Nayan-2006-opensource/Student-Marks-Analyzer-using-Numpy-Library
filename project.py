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

percentage=total/5 #percentage of each student
for i in range(len(percentage)):
    print("percentage of student",student[i],"is",percentage[i])

#highest and lowest scorer
high=np.argmax(total)
print("the highest scorer in the class is",student[high])

low=np.argmin(total)
print("the lowest scorer in the class is",student[low])


#class average
class_avg=np.mean(total)
print("the avg of the class is ",class_avg)

#subject wise analysis

#sub wise highest and lowest marks marks
for i in range(len(subject)):
    arr=marks[:,i]
    a=marks[:,i]
    max_score=np.argmax(arr)
    min_score=np.argmin(a)
    print("the highest score in",subject[i],"is ",arr[max_score])
    
    print("the lowest score in",subject[i],"is",a[min_score])

 #Average  of each subject

for i in range(len(subject)):
    avg_marks=marks[:,i]
    Average=np.mean(avg_marks)
    print("the average marks in subject",subject[i],"=",Average)

    
#hardest and easiest subject
total=np.mean(marks,axis=0)
hardest=np.argmin(total)
print("the hardest subject is",subject[hardest],"having average of",total[hardest])
easiest=np.argmax(total)
print("the easiest subject is",subject[easiest],"having average of",total[easiest])

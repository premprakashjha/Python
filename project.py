students=input('Enter the name of students: ').split(',')
marks=list(map(int,input('Enter the marks of the students: ').split(',')))
updates=list(map(int,input('Enter the marks to be updated: ').split(',')))
updated_marks=[x+i for x,i in zip(marks,updates)]
record=dict(zip(students,marks))
updated_record=dict(zip(students,updated_marks))
marks.sort(key=None,reverse=True)
sorted_record={}
for i in marks:
for j in students:
if record[j]==i:
sorted_record[j]=i
updated_marks.sort(key=None,reverse=True)
sorted_uprecord={}
for i in updated_marks:
for j in students:
if updated_record[j]==i:
sorted_uprecord[j]=i
k=list(record.keys())
v=list(record.values())
print('Student\tMarks')
[print(f'{k[i]}\t\t{v[i]}') for i in range(len(k))]
print(sorted_uprecord)
first_ranker=list(sorted_uprecord.keys())[0]
n=list(sorted_record).index(first_ranker)
print(f'{first_ranker} jumped {n} positions'

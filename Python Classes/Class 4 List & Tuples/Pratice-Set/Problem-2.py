marks = []

s1 = int(input('Student 1 Enter your Marks : '))
s2 = int(input('Student 2 Enter your Marks : '))
s3 = int(input('Student 3 Enter your Marks : '))
s4 = int(input('Student 4 Enter your Marks : '))
s5 = int(input('Student 5 Enter your Marks : '))
s6 = int(input('Student 6 Enter your Marks : '))

marks.append(s1)
marks.append(s2)
marks.append(s3)
marks.append(s4)
marks.append(s5)
marks.append(s6)

marks.sort()

print(marks)
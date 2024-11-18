grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
a = [5, 3, 3, 5, 4]
aa = sum(a)/len(a)
b = [2, 2, 2, 3]
bb = sum(b)/len(b)
j = [4, 5, 5, 2]
jj = sum(j)/len(j)
k = [4, 4, 3]
kk = sum(k)/len(k)
s = [5, 5, 5, 4, 5]
ss = sum(s)/len(s)
grades = (aa, bb, jj, kk, ss)
rating = dict(zip(students,grades))
print(rating)



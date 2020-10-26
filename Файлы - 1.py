import os
a, b, c = map(str, input().split())
file = open("text3.txt", "w")
file.write(a)
file.write(" ")
file.write(b)
file.write(" ")
file.write(c)
file.write(" ")
file = open("text3.txt", "r")
k = file.readlines()
s = k[0]
T = s.split(" ")
summ = 0
print(T)
for i in range(3):
    summ += int(T[i])
print(summ)

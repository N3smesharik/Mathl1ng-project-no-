import os.path
import os
file = open("text.txt", "w")
n = int(input("Сколько строк?"))
for i in range(n):
    s = input()
    file.write(s)
file = open("text.txt", "r")
A = ""
for i in range(n):
    text = file.readline()
    A += text + " "
D = A.split(" ")
Res = set(A)
file = open("res.txt", "w")
file.write(str(len(Res)))
print(str(len(Res)))
file.close()
    

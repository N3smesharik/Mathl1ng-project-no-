import os.path
import os
file = open("text.txt", "w")
s = input()
file.write(s)
file = open("text.txt", "r")
s = file.read()
S = s.split(" ")
A = set()
file = open("res.txt", "w")
for n in S:
    if n in A:
        print('YES')
        file.write('YES\n')
    else:
        print('NO')
        file.write('NO\n')
        A.add(n)
file.close()

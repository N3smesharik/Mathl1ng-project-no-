import os.path
import os
file = open("text.txt", "w")
s = input()
file.write(s)
file = open("text.txt", "r")
s = file.read()
S = s.split(" ")
A = [1] * len(S)
for i in range(len(S)):
    A[i] = int(S[i])
b = len(set(A))
print(b)
file = open("text.txt", "w")
file.write(str(b))
file.close()

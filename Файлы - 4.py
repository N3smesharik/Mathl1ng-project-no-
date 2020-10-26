import os.path
import os
file = open("text.txt", "w")
n = int(input("Сколько строк?"))
for i in range(n):
    s = input()
    file.write(s)
file1 = open("text1.txt", "w")
n = int(input("Сколько строк?"))
for i in range(n):
    s = input()
    file.write(s)
file.close()
file1.close()
if not (os.path.isfile("text.txt")) or not(os.path.isfile("text1.txt")):
    print("Error")
elif  os.path.getsize("text.txt") >  os.path.getsize("text1.txt"):
    os.rename("text.txt", "bigger.txt")
    os.rename("text1.txt", "lower.txt")
else:
    os.rename("text.txt", "lower.txt")
    os.rename("text.txt", "bigger.txt")
    
#5 не совсем понял, как делать

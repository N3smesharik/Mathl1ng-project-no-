file = open("text.txt", "w")
n = int(input("Сколько строк?"))
for i in range(n):
    s = input()
    file.write(s)
file = open("text.txt", "r")
A = []
res = 0
for i in range(n):
    text = file.readline()
    A = text.split(" ")
    res += len(A)
print(res, n)

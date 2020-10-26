import re
import os
with open('text.txt', 'w') as file:
    file.write(input())
file = open('text.txt', 'r')
f = file.read()
p1 = r"\b[aeiouyаиеюэяуоё]\S+"
A1 = re.findall(p1, f)
print(*A1)
    
#Исключения вышлю позже, с паттернами всё не очень. Не совсем разобрался, как их записывать

import math
import random
from datetime import datetime
import time
n = random.randint(1000, 1999)
A = []
while True:
    i = int(input())
    if n % i == 0:
        A.append(i)
    else:
        print("Лох. Ты угадал следующие делители:", *A)
        break
d = datetime.now().date()
t = datetime.now().time()
print(d, t)
print("Сколько ждать?")
n = int(input())
while True:
    if n > 0:
        time.sleep(n)
        print("Сколько ждать?")
        n = int(input())
    else:
        print("Го жечь жидов?")
        break

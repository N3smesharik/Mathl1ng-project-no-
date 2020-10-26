import re

t = input()
p1 = r"8\d{10}"
p2 = r"[\w.-]+@[\w.-]+\.?[\w]+?"
A1 = re.findall(p1, t)
A2 = re.findall(p2, t)
print(*A1, *A2)

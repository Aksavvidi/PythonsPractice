#String traverse example
s = "Coding Factory"

#Απλή for
for i in range(len(s)):
    print(s[i], end='')

print()

#Enhanced for
for char in s:
    print(char, end="")

print()

for i in range(1, 10, 2):
    print(i)

print()

s1 = s[7:9]
s2 = s[:6]
s3 = s[7:]
s4 = s[:]
print(s1)
print(s2)
print(s3)
print(s4)

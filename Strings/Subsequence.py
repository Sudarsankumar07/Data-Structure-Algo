# Subsequence of a string

s = "abc"

emp = []

for i in range(1 << len(s)):
    e = ""
    for j in range(len(s)):
        if (i >> j) & 1:
            e += s[j]
    emp.append(e)

print(emp)
# ['', 'a', 'b', 'ab', 'c', 'ac', 'bc', 'abc']
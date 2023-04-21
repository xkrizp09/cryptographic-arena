#!/usr/bin/env python3

with open("message.txt") as filp:
    contents = filp.read()

flag = []
for i in range(0, len(contents), 3):
    chunk = contents[i:i+3]

    if len(chunk) < 3:
        chunk += ' ' * (3 - len(chunk))

    a, b, c = chunk
    flag.append(c + a + b)

flag = "".join(flag).split()[-1]
print(flag)
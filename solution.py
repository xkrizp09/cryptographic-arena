#!/usr/bin/env python3

import binascii
from operator import xor

with open("output2.txt") as h:
    encrypted_test = bytearray.fromhex(h.readline().strip())
    encrypted_flag = bytearray.fromhex(h.readline().strip())

blob = bytearray(a ^ b for a, b in zip(encrypted_test, encrypted_flag))
test = b"No right of private conversation was enumerated in the Constitution. I don't suppose it occurred to anyone at the time that it could be prevented."

flag = bytearray(a ^ b for a, b in zip(blob, test[: len(encrypted_flag)]))
print(f"{flag=}")
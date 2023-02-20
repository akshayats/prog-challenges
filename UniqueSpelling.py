#!/usr/bin/env python3
import sys

print("Hello World")
# for line in sys.stdin:
word = 'nonoo o'

a = word
b = word[1:]+word[-1]
# ans = list(a) list(b)
ans = [j for i, j in zip(a, b) if i != j]
ans = ''.join([word[0]]+ans)
print(ans)

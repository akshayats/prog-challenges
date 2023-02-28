#!/usr/bin/env python3
import sys

for word in sys.stdin:
    word_shift = word[1:]+word[-1]  # Word shifted by 1 char, pad with last char
    ans = [j for j, i in zip(word_shift, word) if j != i]  # Look back 1 char
    ans = ''.join([word[0]]+ans)  # first char
    print(ans)

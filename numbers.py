#!/usr/bin/env python3

total = 0
n = 10

for i in range(0, n):
    for j in range(0, n):
        for k in range(0, n):
            if (i == 0 and j == 0 and k == 0):
                continue

            if i + j == k:
                total += 1
                continue

            if i - j == k:
                total += 1
                continue

            if i * j == k:
                total += 1
                continue

            if j > 0:
                if i / j == k:
                    total += 1
                    continue


print(total)

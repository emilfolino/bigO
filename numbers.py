#!/usr/bin/env python3

numbers = []

def add_numbers(i, j, k, typ):
    numbers.append({'i':i, 'j':j, 'k':k, 'typ':typ})

for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            if i + j == k:
                add_numbers(i, j, k, "+")

            if i - j == k:
                add_numbers(i, j, k, "-")

            if i * j == k:
                add_numbers(i, j, k, "*")

            if j > 0:
                if i / j == k:
                    add_numbers(i, j, k, "/")


print(str(len(numbers)))

print(numbers)

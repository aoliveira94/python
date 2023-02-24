#!/usr/bin/env python3

__version__ = "0.1.0"
__author__ = "Aoliveira"

list_number =  list(range(1, 11))

for n1 in list_number:
    print("{:-^18}".format(f"Tabuada do {n1}"))
    print()
    for n2 in list_number:
        result = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {result}"))
    print("\n","#" * 18)
    print()
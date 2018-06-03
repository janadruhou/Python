#!/usr/bin/env python3

print("Zadávejte celá čísla, za každým enter: nebo ^D nebo ^Z pro ukončení")

total = 0
count = 0

while True:
    try:
        line = input()
        if line:
            number = int(line)
            total += number
            count += 1
        except ValueError as err:
            print(err)
            continue
        except E0FError:
            break

if count:
    print("počet =", count,"celkem =", total, "průměr =", total/count)




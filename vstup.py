#!/usr/bin/env python3

print("Zadávejte celá čísla a potvrďte ENTER. Pro ukončení stiskněte ENTER bez zadání čísla")

total = 0
count = 0

while True:
    line = input("číslo: ")
    if line:
        try:
            number = int(line)
        except ValueError as err:
            print(err)
            continue
        total += number
        count += 1
    else:
        break
if count:
    print("počet =", count, "celkem =", total, "průměr =", total/count)


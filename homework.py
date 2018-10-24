small = None
large = None

next_iteration = True
while next_iteration:
    value = raw_input("Enter name: ")

    try:
        number = int(value)
    except ValueError as e:
        print("Invalid input")
        if value == 'done':
            next_iteration = False
        continue

    if large is None:
        large = number
    
    if large < number:
        large = number

    if small is None:
        small = number
    
    if small > number:
        small = number

print(large)
print(small)




#!/usr/bin/python3

def get_int(msg):
    while True:
        try:
            i = int(input(msg))
            return i
        except VallueError as err:
            print(err)

age = get_int("zadej svůj věk: ")


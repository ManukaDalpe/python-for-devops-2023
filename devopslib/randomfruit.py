from random import choices


def fruit():
    fruits = ["apple", "cherry", "mango"]
    return choices(fruits)[0]

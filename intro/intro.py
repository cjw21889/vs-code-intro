import pandas as pd
import requests


def double(num):
    return num * 2


def triple(num):
    """this returns input times three

    Args:
        num (int): number
    """
    return num * 3


# print('hello world')
# print(double(5))
# print( "hello")
# print(triple(8))

# string = "Hello"
# print(string.upper())

name = input("What's your name?")
print(f"{name} is lame")

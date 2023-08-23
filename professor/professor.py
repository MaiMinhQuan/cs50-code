import random

def main():

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                continue
        except:
            continue

def generrate_integer(level):
    
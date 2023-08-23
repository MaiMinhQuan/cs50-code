import random

def main():
    score = 0
    level = get_level()
    for i in range(2):
        x = generate_integer(level)
        y = generate_integer(level)
        result = x + y
        count = 0
        while count<4:
            print(f"{x} + {y} = ", end="")
            ans = input()
            count+=1
            if ans.isdigit() == False or int(ans) != result:
                print("EEE")
                continue
            else:
                score+=1
                break
        if count == 3:
            print(f"{x} + {y} = {result}")
    print(f"Score: {score}")

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

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()
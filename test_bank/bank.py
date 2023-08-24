def main():
    s = input("Greeting: ")
    print(f"${value(s)}")

def value(greeting):
    s = greeting.lower().strip()
    if s[0:5] == "hello":
        return 0
    elif s[0] == "h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()

def main():
    s = input("Input: ")
    s = shorten(s)
    print(f"Output: {s}")

def shorten(word):
    s = ""
    for i in word:
        if i not in ["u", "e", "o", "a", "i", "U", "E", "O", "A", "I"]:
            s+=i
    return s

if __name__ == "__main__":
    main()
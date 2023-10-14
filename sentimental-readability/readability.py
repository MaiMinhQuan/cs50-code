def cnt(s):
    letters = 0
    words = 0
    sentences = 0
    for c in s:
        if c.isalpha():
            letters += 1
        if c == " ":
            words += 1
        if c == "." or c == "?" or c == "!":
            sentences += 1

    return letters, words + 1, sentences


def main():
    s = input("Text: ")
    l, w, s = cnt(s)
    lw = l / w * 100
    sw = s / w * 100
    result = 0.0588 * lw - 0.296 * sw - 15.8
    if result >= 16:
        print("Grade 16+")
    elif result < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {int(result + 0.5)}")


main()

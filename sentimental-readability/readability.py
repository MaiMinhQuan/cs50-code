def cnt(s):
    letters = 0
    words = 0
    sentences = 0
    for c in s:
        if c.isalpha():
            letters++
        if c == " ":
            sentences++


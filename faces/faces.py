def convert(s):
    s=s.replace(":)", "🙂")
    s=s.replace(":(", "🙁")
    return s
def main():
    s=input()
    print(convert(s))

main()
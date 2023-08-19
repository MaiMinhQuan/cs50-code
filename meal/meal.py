def main():
    s = input("What time is it? ")
    t = convert(s)
    if 7<=t<=8:
        print("breakfast time")
    elif 12<=t<=13:
        print("lunch time")
    elif 18<=t<=19:
        print("dinner time")

def convert(s):
    x,y = s.split(":")
    time = float(x)+float(y)/60
    return time

if __name__ == "__main__":
    main()
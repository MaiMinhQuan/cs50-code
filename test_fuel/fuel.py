def main():
    i = input("Fraction: ")
    value = convert(i)
    print(gauge(value))
def convert(i):
    while True:
        try:
            if "/" not in i:

            ts, ms = i.split("/")
            ts = int(ts)
            ms = int(ms)
            f = ts/ms
            if f<=1:
                f*=100
                return f
            else:
                i = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise

def gauge(i):
    if i <= 1:
        return "E"
    elif i >= 99:
        return "F"
    else:
        return f"{i}%"

if __name__ == "__main__":
    main()
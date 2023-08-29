from validator_collection import validators

def main():
    s = input("What 's your email address? ")
    try:
        hl = validators.email(s)
        print("Valid")
    except:
        print("Invalid")

if __name__ == "__main__":
    main()
    
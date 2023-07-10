from validator_collection import validators, errors

def main():
    print(validate(input("What's your email adress? ")))

def validate(s):
    try:
        email = validators.email(s)
        return "Valid"
    except errors.EmptyValueError:
        return "Invalid"
    except errors.InvalidEmailError:
        return "Invalid"




if __name__ == "__main__":
    main()
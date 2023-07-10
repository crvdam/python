from datetime import date, timedelta
import sys, inflect

p = inflect.engine()

def main():
    print(get_delta(input("Date of Birth: ")), "minutes")



def get_delta(s):
    try:
        geboorte = date.fromisoformat(s)
        vandaag = date.today()
        verschil = vandaag - geboorte
        verschil = verschil.days * 24 * 60
        return p.number_to_words(verschil, andword="").capitalize()


    except ValueError:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()
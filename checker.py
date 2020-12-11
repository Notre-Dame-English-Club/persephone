from csv import DictReader, DictWriter
from difflib import SequenceMatcher as sm

def match(original, input):
    return sm(None, original.lower(), input.lower()).ratio()

def check(name, roll):
    with open('studentdb.csv', "r", encoding="utf-8") as csvfile:
        reader = DictReader(csvfile)
        for row in reader:
            if roll==row['College Roll']:
                result = match(row['Name'], name)
                print(result)
                if result>=.8:
                    return True
        return False
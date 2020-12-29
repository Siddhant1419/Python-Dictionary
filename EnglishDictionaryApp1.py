import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def meaning(value):
    value = value.lower()
    if value in data:
        return data[value]
    elif len(get_close_matches(value, data.keys())) > 0:
        yon = input("Did you mean %s instead? Enter Y if yes or N if no: " % get_close_matches(value,data.keys())[0])
        if yon == "Y":
            return data[get_close_matches(value,data.keys())[0]]
        elif yon == "N":
            return "The word does not exist. Please double check your word."
        else:
            return "We didn't understand your input. Please answer in Y or N. Thank you."
    else:
        print("The word does not exist. Please recheck the word.")

word = input("Enter a Word: ")

output = (meaning(word))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
    
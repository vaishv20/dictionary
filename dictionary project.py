from difflib import get_close_matches

import json
data = json.load(open('dictionary.json'))
def translate(word):
    word = word.lower()
    if (word in data):
        return data[word]
    elif len(get_close_matches(word, data.keys())):
        y = input("Do you mean %s instead? Enter y if yes and n if no:" % get_close_matches(word, data.keys())[0])
        y = y.lower()
        if (y =="y"):
            return data[get_close_matches(word, data.keys())[0]]
        elif (y == "n"):
            return ("The word doesn't exist. Please double check it.") 
        else:
            return ("We did not understand the entry.")      
    else:
        return ("The word doesn't exist. Please double check it.")

word = input("Enter the word:")
output = translate(word)
if type(output)== list:
    for item in output:
        print(item)
else :
    print(output)        
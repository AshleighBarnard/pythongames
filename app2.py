import json
data = json.load(open("data"))

def translate(w):
    return data[w]

word = input("Enter Word: ")

print(translate(word))

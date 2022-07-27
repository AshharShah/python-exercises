from typing import Set


dict = {
    "Set": "put, lay, or stand (something) in a specified place or position.",
    "Eat": "put (food) into the mouth and chew and swallow it.",
    "Sleep": "a condition of body and mind that typically recurs for several hours every night, in which the nervous system is relatively inactive, the eyes closed, the postural muscles relaxed, and consciousness practically suspended.",
    "Repeat": "something that occurs or is done again."
}

userInp = input("Enter word to find its meaning: ")
print(dict[userInp])

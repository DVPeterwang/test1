import string
import time

letter = ""
def check(thing, letter):
    if thing[0] != letter:    
        print("the begining is " + letter)
    else:
        pass
def manything(letter):
    timefirst = time.time()
    print("\nthe letter is " + letter)
    boy = input("enter a boy name starting with this letter:")
    boy = boy.lower()
    check(boy, letter)
    girl = input("enter a girl name starting with this letter:")
    girl = girl.lower()
    check(girl, letter)
    animal = input("enter a animal name starting with this letter:")
    animal = animal.lower()
    check(animal, letter)
    place = input("enter a place name starting with this letter:")
    place = place.lower()
    check(place, letter)
    food = input("enter a food name starting with this letter:")
    food = food.lower()
    check(food, letter)
    thing = input("enter a thing name starting with this letter:")
    thing = thing.lower()
    check(thing, letter)
    
    time_now = time.time()
    print("you have used " + str(round(time_now - timefirst)) + " seconds")
letters = list(string.ascii_lowercase)
ask = input("'abc' fast or slow?:")

if ask == "fast":
    start_enter = input("press enter to start,when it starts press ctrl+c to stop:")
    try:
        while True:
            for i in range(25):
                letter = letters[i]
                time.sleep(1)
    except:
        manything(letter)
        
elif ask == "slow":
    start_enter = input("press enter start to start,when it starts press ctrl+c to stop:")
    try:
        while True:
            for i in range(25):
                letter = letters[i]
                time.sleep(1.5)
    except:
        manything(letter)
import string
import time

letter = ""
times = 0


def fast_or_slow(tim):
    global letter, letters
    start_enter = input("press enter to start,when it starts press ctrl+c to stop:")
    try:
        while True:
            for i in range(25):
                letter = letters[i]
                time.sleep(tim)
    except:
        while True:
            ask_rw = manything(letter)
            if ask_rw == "error":
                continue
            else:
                break


def check(thin, letter):
    if thin[0] != letter:    
        print("the begining is " + letter + " but not " + thin[0])
        return "wrong"
    else:
        return "right"


def manything(letter):
    global times
    times += 1        
    timefirst = time.time()
    print("\nthe letter is " + letter)
    
    boy = input("enter a boy name starting with this letter:")
    boy = boy.lower() 
    cs = check(boy, letter)
    
    if cs == "wrong":
        return "error"
    
    girl = input("enter a girl name starting with this letter:")
    girl = girl.lower()
    cs = check(girl, letter)
    
    if cs == "wrong":
        return "error"
    animal = input("enter a animal name starting with this letter:")
    animal = animal.lower()
    cs = check(animal, letter)
    
    if cs == "wrong":
        return "error"
    
    place = input("enter a place name starting with this letter:")
    place = place.lower()
    cs = check(place, letter)
    
    if cs == "wrong":
        return "error"
    food = input("enter a food name starting with this letter:")
    food = food.lower()
    cs = check(food, letter)
    
    if cs == "wrong":
        return "error"
    
    thing = input("enter a thing name starting with this letter:")
    thing = thing.lower()
    cs = check(thing, letter)
    
    if cs == "wrong":
        return "error"
    
    time_now = time.time()
    
    print("you have used " + str(round(time_now - timefirst)) + " seconds")
    print("you have used " + str(times) + " times")
    
    return "success"


letters = list(string.ascii_lowercase)
ask = input("'abc' fast or slow?:")

if ask == "fast":
    fast_or_slow(1)
        
elif ask == "slow":
    fast_or_slow(1.5)
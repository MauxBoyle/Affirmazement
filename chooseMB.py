# nested if practice

suggests = [] # I need this to be stored externally, not reset at each play.

def RoomB01(previous, choice):
    oblique = 'Do we need holes?'
    affirmation = 'tbd'
    current = "B01"
    print(f"You were in {previous}. You chose {choice}. Now you're in {current}")
    print(oblique)
    print(affirmation)
    print("1. First choice")
    print("2. Second choice")
    new_choice = input("> ")

    if new_choice == '1':
        RoomC01(current, new_choice)
    elif new_choice == '2':
        RoomC02(current, new_choice)
    else:
        print("Not a strategy I'd considered, but I'll make a note of it for next time.")
        suggests.append((current, new_choice))
        RoomB01("B01","to go off book")

def RoomB02(previous, choice):
    oblique = 'Would anybody want it?'
    affirmation = 'tbd'
    current = "B02"
    print(f"You were in {previous}. You chose {choice}. Now you're in {current}")
    print(oblique)
    print(affirmation)
    print("1. First choice")
    print("2. Second choice")
    print("3. Sometimes there's a third choice.")
    new_choice = input("> ")

    if new_choice == '1':
        RoomC03(current, new_choice)
    elif new_choice == '2':
        RoomC04(current, new_choice)
    elif new_choice == '3':
        RoomC05(current, new_choice)
    else:
        print("Not a strategy I'd considered, but I'll make a note of it for next time.")
        suggests.append((current, new_choice))
        RoomB02("B02","to go off book")

def RoomC01(previous, choice):
    oblique = 'Disconnect from desire.'
    affirmation = 'tbd'
    current = "C01"
    print(f"You were in {previous}. You chose {choice}. Now you're in {current}")
    print(oblique)
    print(affirmation)
    print("1. First choice")
    print("2. Second choice")
    new_choice = input("> ")

    if new_choice == '1':
        RoomD01(current, new_choice)
    elif new_choice == '2':
        RoomD02(current, new_choice)
    else:
        print("Not a strategy I'd considered, but I'll make a note of it for next time.")
        suggests.append((current, new_choice))
        RoomC01("C01","to go off book")

def RoomC02(previous, choice):
    oblique = 'Use filters.'
    affirmation = 'tbd'
    current = "C02"
    print(f"You were in {previous}. You chose {choice}. Now you're in {current}")
    print(oblique)
    print(affirmation)
    print("1. First choice")
    print("2. Second choice")
    new_choice = input("> ")

    if new_choice == '1':
        RoomD02(current, new_choice)
    elif new_choice == '2':
        RoomD03(current, new_choice)
    else:
        print("Not a strategy I'd considered, but I'll make a note of it for next time.")
        suggests.append((current, new_choice))
        RoomC02("C02","to go off book")

def RoomC03(previous, choice):
    oblique = 'Define an area as "safe" and use it as an anchor.'
    affirmation = 'tbd'
    current = "C03"
    print(f"You were in {previous}. You chose {choice}. Now you're in {current}")
    print(oblique)
    print(affirmation)
    print("1. First choice")
    print("2. Second choice")
    new_choice = input("> ")

    if new_choice == '1':
        RoomD03(current, new_choice)
    elif new_choice == '2':
        RoomD04(current, new_choice)
    else:
        print("Not a strategy I'd considered, but I'll make a note of it for next time.")
        suggests.append((current, new_choice))
        RoomC03("C03","to go off book")

def RoomC04(previous, choice):
    oblique = 'Courage!'
    affirmation = 'tbd'
    current = "C04"
    print(f"You were in {previous}. You chose {choice}. Now you're in {current}")
    print(oblique)
    print(affirmation)
    print("1. First choice")
    print("2. Second choice")
    new_choice = input("> ")

    if new_choice == '1':
        Roomxx(current, new_choice)
    elif new_choice == '2':
        Roomxx(current, new_choice)
    else:
        print("Not a strategy I'd considered, but I'll make a note of it for next time.")
        suggests.append((current, new_choice))
        RoomC04("C04","to go off book")

def RoomC05(previous, choice):
    oblique = 'Use an unacceptable color.'
    affirmation = 'tbd'
    current = "C05"
    print(f"You were in {previous}. You chose {choice}. Now you're in {current}")
    print(oblique)
    print(affirmation)
    print("1. First choice")
    print("2. Second choice")
    print("3. Sometimes there's a third choice.")
    new_choice = input("> ")

    if new_choice == '1':
        RoomD06(current, new_choice)
    elif new_choice == '2':
        RoomD07(current, new_choice)
    elif new_choice == '3':
        RoomD08(current, new_choice)
    else:
        print("Not a strategy I'd considered, but I'll make a note of it for next time.")
        suggests.append((current, new_choice))
        RoomC05("C05","to go off book")

def RoomD01(previous, choice):
    oblique = 'You are an engineer.'
    affirmation = 'tbd'
    current = "D01"
    print(f"You were in {previous}. You chose {choice}. Now you're in {current}")
    print(oblique)
    print(affirmation)
    print("1. First choice")
    print("2. Second choice")
    new_choice = input("> ")

    if new_choice == '1':
        Roomxx(current, new_choice)
    elif new_choice == '2':
        Roomxx(current, new_choice)
    else:
        print("Not a strategy I'd considered, but I'll make a note of it for next time.")
        suggests.append((current, new_choice))
        RoomD01("D01","to go off book")

def RoomD02(previous, choice):
    oblique = 'Decorate. Decorate.'
    affirmation = 'tbd'
    current = "D02"
    print(f"You were in {previous}. You chose {choice}. Now you're in {current}")
    print(oblique)
    print(affirmation)
    print("1. First choice")
    print("2. Second choice")
    new_choice = input("> ")

    if new_choice == '1':
        RoomE02(current, new_choice)
    elif new_choice == '2':
        RoomE03(current, new_choice)
    else:
        print("Not a strategy I'd considered, but I'll make a note of it for next time.")
        suggests.append((current, new_choice))
        RoomD02("D02","to go off book")

def RoomD03(previous, choice):
    oblique = 'Do the words need changing?'
    affirmation = 'tbd'
    current = "D03"
    print(f"You were in {previous}. You chose {choice}. Now you're in {current}")
    print(oblique)
    print(affirmation)
    print("1. First choice")
    print("2. Second choice")
    new_choice = input("> ")

    if new_choice == '1':
        RoomE04(current, new_choice)
    elif new_choice == '2':
        RoomE05(current, new_choice)
    else:
        print("Not a strategy I'd considered, but I'll make a note of it for next time.")
        suggests.append((current, new_choice))
        RoomD03("D03","to go off book")

def RoomD04(previous, choice):
    oblique = 'Which elements can be grouped?'
    affirmation = 'tbd'
    current = "D04"
    print(f"You were in {previous}. You chose {choice}. Now you're in {current}")
    print(oblique)
    print(affirmation)
    print("1. First choice")
    print("2. Second choice")
    new_choice = input("> ")

    if new_choice == '1':
        RoomE05(current, new_choice)
    elif new_choice == '2':
        RoomE06(current, new_choice)
    else:
        print("Not a strategy I'd considered, but I'll make a note of it for next time.")
        suggests.append((current, new_choice))
        RoomD04("D04","to go off book")

def RoomD05(previous, choice):
    oblique = 'Distorting time'
    affirmation = 'tbd'
    current = "D05"
    print(f"You were in {previous}. You chose {choice}. Now you're in {current}")
    print(oblique)
    print(affirmation)
    print("1. First choice")
    print("2. Second choice")
    new_choice = input("> ")

    if new_choice == '1':
        RoomE07(current, new_choice)
    elif new_choice == '2':
        RoomE08(current, new_choice)
    else:
        print("Not a strategy I'd considered, but I'll make a note of it for next time.")
        suggests.append((current, new_choice))
        RoomD05("D05","to go off book")

def RoomD06(previous, choice):
    oblique = 'Turn it upside down.'
    affirmation = 'tbd'
    current = "D06"
    print(f"You were in {previous}. You chose {choice}. Now you're in {current}")
    print(oblique)
    print(affirmation)
    print("1. First choice")
    print("2. Second choice")
    new_choice = input("> ")

    if new_choice == '1':
        RoomE08(current, new_choice)
    elif new_choice == '2':
        RoomE09(current, new_choice)
    else:
        print("Not a strategy I'd considered, but I'll make a note of it for next time.")
        suggests.append((current, new_choice))
        RoomD06("D06","to go off book")

def RoomD07(previous, choice):
    oblique = 'Discover the recipes you are using and abandon them.'
    affirmation = 'tbd'
    current = "D07"
    print(f"You were in {previous}. You chose {choice}. Now you're in {current}")
    print(oblique)
    print(affirmation)
    print("1. First choice")
    print("2. Second choice")
    new_choice = input("> ")

    if new_choice == '1':
        RoomE09(current, new_choice)
    elif new_choice == '2':
        RoomE10(current, new_choice)
    else:
        print("Not a strategy I'd considered, but I'll make a note of it for next time.")
        suggests.append((current, new_choice))
        RoomD07("D07","to go off book")

def RoomD08(previous, choice):
    oblique = 'Are there sections? Consider transitions.'
    affirmation = 'tbd'
    current = "D08"
    print(f"You were in {previous}. You chose {choice}. Now you're in {current}")
    print(oblique)
    print(affirmation)
    print("1. First choice")
    print("2. Second choice")
    new_choice = input("> ")

    if new_choice == '1':
        RoomE11(current, new_choice)
    elif new_choice == '2':
        RoomE12(current, new_choice)
    else:
        print("Not a strategy I'd considered, but I'll make a note of it for next time.")
        suggests.append((current, new_choice))
        RoomD08("D08","to go off book")

def RoomE01(previous, choice):
    oblique = 'Look closely at the most embarrassing details and amplify them.'
    affirmation = 'tbd'
    current = "E01"
    print(f"You were in {previous}. You chose {choice}. Now you're in {current}")
    print(oblique)
    print(affirmation)
    print("The game is over.")

def RoomE02(previous, choice):
    oblique = "Don't be afraid of things because they are easy to do."
    affirmation = 'tbd'
    current = "E02"
    print(f"You were in {previous}. You chose {choice}. Now you're in {current}")
    print(oblique)
    print(affirmation)
    print("The game is over.")

def RoomE03(previous, choice):
    oblique = 'Do something boring.'
    affirmation = 'tbd'
    current = "E03"
    print(f"You were in {previous}. You chose {choice}. Now you're in {current}")
    print(oblique)
    print(affirmation)
    print("The game is over.")

def RoomE04(previous, choice):
    oblique = 'Ask your body.'
    affirmation = 'tbd'
    current = "E04"
    print(f"You were in {previous}. You chose {choice}. Now you're in {current}")
    print(oblique)
    print(affirmation)
    print("The game is over.")

def RoomE05(previous, choice):
    oblique = 'Look at the order in which you do things.'
    affirmation = 'tbd'
    current = "E05"
    print(f"You were in {previous}. You chose {choice}. Now you're in {current}")
    print(oblique)
    print(affirmation)
    print("The game is over.")

def RoomE06(previous, choice):
    oblique = "Where's the edge? Where does the frame start?"
    affirmation = 'tbd'
    current = "E06"
    print(f"You were in {previous}. You chose {choice}. Now you're in {current}")
    print(oblique)
    print(affirmation)
    print("The game is over.")

def RoomE07(previous, choice):
    oblique = 'Ask people to work against their better judgment.'
    affirmation = 'tbd'
    current = "E07"
    print(f"You were in {previous}. You chose {choice}. Now you're in {current}")
    print(oblique)
    print(affirmation)
    print("The game is over.")

def RoomE08(previous, choice):
    oblique = 'Tidy up.'
    affirmation = 'tbd'
    current = "E08"
    print(f"You were in {previous}. You chose {choice}. Now you're in {current}")
    print(oblique)
    print(affirmation)
    print("The game is over.")

def RoomE09(previous, choice):
    oblique = 'Breathe more deeply.'
    affirmation = 'tbd'
    current = "E09"
    print(f"You were in {previous}. You chose {choice}. Now you're in {current}")
    print(oblique)
    print(affirmation)
    print("The game is over.")

def RoomE10(previous, choice):
    oblique = 'Destroy nothing. Destroy the most important thing.'
    affirmation = 'tbd'
    current = "E10"
    print(f"You were in {previous}. You chose {choice}. Now you're in {current}")
    print(oblique)
    print(affirmation)
    print("The game is over.")

def RoomE11(previous, choice):
    oblique = 'Towards the insignificant.'
    affirmation = 'tbd'
    current = "E11"
    print(f"You were in {previous}. You chose {choice}. Now you're in {current}")
    print(oblique)
    print(affirmation)
    print("The game is over.")

def RoomE12(previous, choice):
    oblique = 'What to maintain?'
    affirmation = 'tbd'
    current = "E12"
    print(f"You were in {previous}. You chose {choice}. Now you're in {current}")
    print(oblique)
    print(affirmation)
    print("The game is over.")

# Main game

oblique = 'Is there something missing?'
affirmation = 'tbd'
current = "A01"
print(f"You are in {current}")
print(oblique)
print(affirmation)
print("1. First choice")
print("2. Second choice")
new_choice = input("> ")

if new_choice == '1':
    RoomB01(current, new_choice)
elif new_choice == '2':
    RoomB02(current, new_choice)
else:
    print("Not a strategy I'd considered, but I'll make a note of it for next time.")
    print("Just this once, I'll pick for you.")
    suggests.append((current, new_choice))
    RoomB01("A01","to go off book")

print(suggests)

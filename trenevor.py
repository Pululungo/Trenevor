boolean_variable = False
string_variable = "Hola tarola"
print ("Welcome to Trenevor")
print()
print ("In this text-based adventure, you'll be taking the steps of a hero trying to escape imprisionment.")
print ("Always mind your Energy, Health and Hours left in order to avoid capture or death.")
print()
classes = ["Warrior", "Mage", "Priest"]
print ("You can choose one of the following classes to play:")
for classes in classes:
        print (classes)
print ()
player_class = False
while player_class == False:
    player_class = input ("Type down your desired class >> ")
    if player_class == "Warrior":
        print("And, What is the name of your fierce Warrior?")
        player_name = input(f"I want my {player_class} to be named >> ")
        player_attack = "Punch"
    elif(player_class == "Priest"):
        print("And, What is the name of your holy Priest?")
        player_name = input(f"I want my {player_class} to be named >> ")
        player_attack = "Smite"
    elif(player_class == "Mage"):
        print("And, What is the name of your arcane Mage?")
        player_name = input(f"I want my {player_class} to be named >> ")
        player_attack = "Hurl a fireball"
    else:
        print("That class is not supported. Please stick to the list.")
        player_class = False
print()
Health = 10
Energy = 10
Hours_left = 4
print("A flash of moonlight reaches your eyes. You find yourself a cold, moisty dungeon. You can't remember how you got there or why you're trapped. All you can hear from the outside is the unmistakable sound of an axe on a grindstone.")
print ("You don't know much, other than you have little time.")
print (f"Luckily for you, you are a resourceful {player_class}, and quickly fashion yourself with tools and weapons to plan your escape.")
if player_class == "Warrior":
    print("With much effort and using your brute strength, you crack a brick from the wall that you can use as a fist weapon. Is not until you weigth the brick in your bloodied hands that you notice a grin in your face. The smell of blood is an old friend, after all.")
elif(player_class == "Priest"):
    print("You close your eyes and whisper a prayer to your deity, and as your words escape the dungeon cell, the echo of divinity reaches your spirit. When you open your eyes, a golden Morningstar sits in your hands. An inscription reads: 'Use it to smite the wicked.'")
elif(player_class == "Mage"):
    print("With both hands open in front of you, you mutter a spell and wait for a response in the arcane... but nothing happens. Your gaze jumps from one corner of the room to another, when suddenly, in the corner, you spot a small iron nail. With it, you start drawing a rune on the floor. With the final stroke, the lines turn alive and almost seem to smolder, only to dim once more. Your pupils now bear this rune, and your hands now respond to the arcane secrets of fire.")
print()
print (f"Your Health is currently {Health}")
print (f"Your Energy is currently {Energy}")
print (f"{Hours_left} hours remain before dawn.")
print()
print("As you study the situation unfolding, you narrow it down to one of the next three options:")
print ()
print("Taunting the guard into attacking you and fight him. (X)")
print("Bursting the door open with your weapon. (Y)") 
print("Wait for a chance to steal the key. (Z)")
print ()
print(f"Which path will the {player_class}  {player_name} take?")
player_d1 = False
while player_d1 == False:
    player_d1 = input("Type the scenario you'll take: 'X', 'Y' or 'Z' >> ")
    print()
    if player_d1 == "X":
        print("You say something about the guard's mother that really pisses him off. With sword unseathed, he opens the door and lunges at you.")
        if player_class == "Warrior":
            print("The fight is short, crude, and intense, but you come out victorious. An ugly wound oozes blood, but this only makes you look more fierce. Before continuing, you take the guard's sword. He ain't gonnna need it anymore.")
            Health = (Health-2)
            Energy = (Energy-2)
        elif player_class == "Priest":
            print("You exchange blows for a while, but you're still getting used to this weapon. It takes a while before you manage to smite the guard with a desicive strike. You're not hurt, but you need to catch a breath before continuing.")
            Health = (Health-2)
            Energy = (Energy-2)
        elif player_class == "Mage":
            print("As soon as he's inside, you hurl a fireball in his face, ending the fight before it starts. You find that you're a bit rustiy on your technique, however, as some flames managed to burn your hands.")
            Health = (Health-1)
    elif(player_d1 == "Y"):
        print("With the tools at your disposal, you start to strike the weak spots in the door.")
        if player_class == "Warrior":
            print("With only a brick to use, it feels like an eternity before you start to see some progress, and  by the time you're done, the skin in your hands and fingers is as good as pulp.")
            Energy = (Energy-4)
            Hours_left = (Hours_left-1)
        if player_class == "Priest":
            print("The morningstar manages to break loose one of the hinges without much effort. The door swings open after a few strikes.")
            Energy = (Energy-1)
        if player_class == "Mage":
            print("You bring your hands together to melt the solid steel with the fire spell. It's quick, but it  drains your stamina.")
            Energy = (Energy-2)
    elif(player_d1 == "Z"):
        print("You sit by the door and bide your time. Eventually, a guard passes by and you manage to pickpocket the keys.")
        Hours_left = (Hours_left-2)
    else:
        print("Please choose a valid scenario: 'X', 'Y' or 'Z'.")
        player_d1 = False

print()
print (f"Your Health is currently {Health}")
print (f"Your Energy is currently {Energy}")
print (f"{Hours_left} hours remain before dawn.")
print()

if Health == 0:
    print("That last blow is too much for your body to handle. You fall to your knees, and die. GAME OVER")
if Energy == 0:
    print("Your legs stop responding to your commands, your hands are too sore to even make a fist. After a short persecuttion, you fall yourself surrounded and fall in the enemy's hands. Your execution will take place immediately. GAME OVER") 
if Hours_left == 0:
    print("You can hear a rooster in the distance, followed shortly by the sound of dozens of footsteps closing in to your position. Time's up, nowhere to hide. GAME OVER")

print("You're out of the cell. Now you have to navigate your way out of the dungeon. Do you...")
print ()
print("Sneak around by waiting for the right moments to pass by. (X)")
print("Look for a distraction to lure the guards away. (Y)") 
print("Fight everything on sight like a battering ram. (Z)")
print ()
print(f"How will {player_name} avoid capture?")
player_d2 = False
while player_d2 == False:
    player_d2 = input("Type the scenario you'll take: 'X', 'Y' or 'Z' >> ")
    print()
    if player_d2 == "X":
        print("You manage to sneak around through the narrow halls by sticking to the shadows, but it takes you quite a while.")
        Hours_left = (Hours_left-2)
    elif(player_d2 == "Y"):
        print("You look for something to lure the guards out of their posts.")
        if player_class == "Warrior":
            print("The best distraction you can think of is to cause a fight, so you yell: '¡Arriba el América!', and all of the sudden, hell breaks loose. You manage to avoid detection amist the chaos.")
            Energy = (Energy-1)
        if player_class == "Priest":
            print("You pray to your deity with all your might, asking for a miracle to manifest itself. After a while, the rock ceiling appears to turn misty, until actual clouds begin to form. It starts to rain on the inside of the dungeon, everyone starts to leave.")
            Energy = (Energy-3)
        if player_class == "Mage":
            print("You spot a few barrels of wheat near the barracks. Dry, flammable wheat. With just a blink of an eye, a spark of fire burts into life near them, and a small fire begins to form. It takes a while before it caches on, but amist the evacuation, you manage to exit as well.")
            Energy = (Energy-2)
    elif(player_d2 == "Z"):
        if player_class == "Warrior":
            print("This is your true calling. The moment you've been waiting for. Stepping in with authority into the barraks, with your weapon at hand, you start to deliver blow after blow. A mortal strike after another. Rage builds up inside you with each strike. Despite recieving several wounds, you've never felt more alive.")
            Health = (Health-3)
            Energy = (Energy-3)
            Hours_left = (Hours_left-1)
        if player_class == "Priest":
            print("You kiss the morning star after a short prayer. Your eyes glow with divine resolution and energy. You may not be a fighter, but this time, violence seems more like divine retribution. You charge against the guards with a might of gods.")
            Health = (Health-4)
            Energy = (Energy-2)
            Hours_left = (Hours_left-1)
        if player_class == "Mage":
            print("You wonder how this barbaric pest managed to imprision someone as gifted as you. You decide that you're not leaving survivors. The power of fire is at your fingertips, and no one other than you will live to tell what happened here today. Your eyes glow with a scorching glow, and fire engulfs the entire barracks.")
            Health = (Health-2)
            Energy = (Energy-4)
            Hours_left = (Hours_left-1)
    else:
        print("Please choose a valid scenario: 'X', 'Y' or 'Z'.")
        player_d2 = False

print()
print (f"Your Health is currently {Health}")
print (f"Your Energy is currently {Energy}")
print (f"{Hours_left} hours remain before dawn.")
print()

if Health == 0:
    print("That last blow is too much for your body to handle. You fall to your knees, and die. GAME OVER")
if Energy == 0:
    print("Your legs stop responding to your commands, your hands are too sore to even make a fist. After a short persecuttion, you fall yourself surrounded and fall in the enemy's hands. Your execution will take place immediately. GAME OVER") 
if Hours_left == 0:
    print("You can hear a rooster in the distance, followed shortly by the sound of dozens of footsteps closing in to your position. Time's up, nowhere to hide. GAME OVER")

print(f"Once outside of the dungeon, things take a strange twist. You hear a familiar voice thundering from above the castle grounds: 'To arms!! The prisioner {player_name} has escaped!! Awaken the Gargoyles to smoke out that sleazy {player_class}!'")
print()
print("Shortly after, the foundations of the entire castle begin to rumble, followed by ")
# 12. Treasure Island game:

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("Before you decide if you want to try your luck finding the treasure, please be aware that the adventure will be very dangerous, so think twice, before you make the decision, because after you start, there won't be a way back.")
decision = input("Please let me know what is your decision by typing up Y or N: ")

if decision == "Y" or decision == "y":
  print('''You are very brave! Now you will get a chance to find one of the most wanted treasures in the world, Captain's Blackbeard treasure. Now you get on a private jet and you will be dropped over your destination. However, after you get to the place, you will still have to make your way through to the treasure. Be aware that many tried before, but so far now one has made it! Be the first one!
        _____
              .-" .-. "-.
            _/ '=(0.0)=' \_
          /`   .='|m|'=.   `\
          \________________ /
      .--.__///`'-,__~\\\\~`
     / /6|__\// a (__)-\\\\
     \ \/--`((   ._\   ,)))
     /  \\  ))\  -==-  (O)(
    /    )\((((\   .  /)))))
   /  _.' /  __(`~~~~`)__
  //"\\,-'-"`   `~~~~\\~~`"-.
 //  /`"              `      `\ ''')
  first_choice = input("You were dropped on a desert island, somwhere in the pacific ocean. You landed in between 2 massive rock mountains. Now there are only 2 ways forward. Which one will you take? Left or right: ")
  if first_choice == "Left" or first_choice == "left":
    print('''After a long walk you get to a massive river.                 _.._
   _________....-~    ~-.______
~~~                            ~~~~-----...___________..--------
                                           |   |     |
                                           | |   |  ||
                                           |  |  |   |
                                           |'. .' .`.|
___________________________________________|0oOO0oO0o|____________
 -          -         -       -      -    / '  '. ` ` \    -    -
      --                  --       --   /    '  . `   ` \    --
---            ---          ---       /  '                \ ---
     ----               ----        /       ' ' .    ` `    \  ----
-----         -----         ----- /   '   '        `      `   \
     .-~~-.          ------     /          '    . `     `    `  \
    (_^..^_)-------           /  '    '      '      `
                    --------/     '     '   ' " ''')
    second_choice = input("Now you look on the map and you know that this is the right path, and to follow it, you need to cross the river. You can either cross it, or wait until you build a raft to get on the other side. What do you do? swim or wait: ")
    if second_choice == "wait" or second_choice == "Wait":
      print('''Well done! You managed to build a raft and you got on the other side. You carry on walking following your map. You get to a huge pyramid. You found the place!
    
                 /\.
                /|_\`.
               /__|_\/`.
              /__|__|\/.`.
             /_|__|__|\/`/`.
            /|__|___|__\/`/
           /__|___|___|_\/ ''')
    
      third_choice = input("You can see 3 doors now and you have to choose which one will you go through to get inside. Which one will you choose? Red, blue, or yellow: ")
      if third_choice == "Yellow" or third_choice == "yellow":
        print('''Congratulations! You found a treasure and you become extremely rich and famous :) *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
******************************************************************************* ''')
      elif third_choice == "red" or third_choice == "Red":
        print('''Unfortunately you made a wrong choice, you get into room full of fire and you get burned in fire :( Game over.  (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' ) ''')
      else:
        print('''You fell into a whole, ending up in a river and got eaten by a huge fish :( Game over.                  ^`.                     o
     ^_              \  \                  o  o
     \ \             {   \                 o
     {  \           /     `~~~--__
     {   \___----~~'              `~~-_     ______          _____
      \                         /// a  `~._(_||___)________/___
      / /~~~~-, ,__.    ,      ///  __,,,,)      o  ______/    \
      \/      \/    `~~~;   ,---~~-_`~= \ \------o-'            \
                       /   /            / /
                      '._.'           _/_/
                                      ';|\ ''')
  
    else:
      print('''When swimming in the river you got eaten by a huge, angry fish :( Game over.                  ^`.                     o
     ^_              \  \                  o  o
     \ \             {   \                 o
     {  \           /     `~~~--__
     {   \___----~~'              `~~-_     ______          _____
      \                         /// a  `~._(_||___)________/___
      / /~~~~-, ,__.    ,      ///  __,,,,)      o  ______/    \
      \/      \/    `~~~;   ,---~~-_`~= \ \------o-'            \
                       /   /            / /
                      '._.'           _/_/
                                      ';|\ ''')
  else:
      print('''You fell into a whole, ending up in a river and got eaten by a huge fish :( Game over.                  ^`.                     o
     ^_              \  \                  o  o
     \ \             {   \                 o
     {  \           /     `~~~--__
     {   \___----~~'              `~~-_     ______          _____
      \                         /// a  `~._(_||___)________/___
      / /~~~~-, ,__.    ,      ///  __,,,,)      o  ______/    \
      \/      \/    `~~~;   ,---~~-_`~= \ \------o-'            \
                       /   /            / /
                      '._.'           _/_/
                                      ';|\ ''')
  
  
    
  
elif decision == "N" or decision == "n":
  print("Maybe you are not the most brave person in the world, but at least you will stay safe :)")
else:
  print("Please make the correct choice!")

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
choice1 = input("You\'ve arrived at a crossroad, which direction would you like to go:\n Left or Right :").lower()
if(choice1 == "left"):
  print("\nGreat Choice!!!, You have come across a lake with an island in between!!")
  choice2 = input("You have 2 choices to choose from: 1)Wait or 2)Swim : \n").lower()
  if(choice2 == "wait"):
    print("\nPatience is always the Key, Nice Job")
    print("One more puzzle and the treasure is all yours")
    
    choice3 = input("\nThere are 2 doors to choose from: 1)Red, 2)Blue, 3)Yellow: ").lower()
    if(choice3 == "yellow"):
      print("\nYou Winn, Congrats!!!")
    elif(choice3 == "red"):
      print("\nGame Over")
    else:
      print("\nGame Over")    
  
  else:
    print("\nAlligators ate you alive\n")
    print('''
                .-._   _ _ _ _ _ _ _ _
 .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
'.___ '    .   .--_'-' '-' '-' _'-' '._
 V: V 'vv-'   '_   '.       .'  _..' '.'.
   '=.____.=_.--'   :_.__.__:_   '.   : :
           (((____.-'        '-.  /   : :
                             (((-'\ .' /
                           _____..'  .'
                          '-._____.-'
    ''')  
    print("\nGAME OVER ")
else:
  print("Lion chased you out of Jungle, it's GAME OVER for you :(")  
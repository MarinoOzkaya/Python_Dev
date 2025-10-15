print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
left_or_right = input("You are at a crossroads. Do you want to go left or right?").lower()
if left_or_right == "left":
    print(r'''  \       /
  \     /  
   \.-./ 
  (o\^/o)  _   _   _     __
   ./ \.\ ( )-( )-( ) .-'  '-.
    {-} \(//  ||   \\/ (   )) '-.
         //-__||__.-\\.       .-'
        (/    ()     \)'-._.-'
        ||    ||      \\
       ('    ('       ')          
    ''')
    print("You are attacked by giant ants and die! Try again")
elif left_or_right == "right":
    print("You make it safely to the next area")
    swim_or_wait = input(
        "You come to a body of water. What will you do? You can swim or wait for a boat. Enter swim or wait").lower()
    if swim_or_wait == "swim":
        print(r'''           ,---,
      _    _,-'    `--,
     ( `-,'            `\
      \           ,    o \
      /   ,       ;       \
     (_,-' \       `, _  ""/
         pb `-,___ =='__,-'
                  ````''')
        print("Piranhas eat you alive! Game over")
    elif swim_or_wait == "wait":
        print(r'''       _~  _~
       __|=|_|=|__
       \ o.o.o.oY/
        \_______/
      ~~~~~~~~~~~~~~''')
        print("A boat carries you to safety")
        door_choice = input(
            "You come to a set of 3 houses. Red, blue, or yellow. Which will you enter? Or will you runaway? Enter red, blue, yellow or run").lower()
        if door_choice == "red":
            print(r'''               (  .      )
                       )           (              )
                             .  '   .   '  .  '  .
                    (    , )       (.   )  (   ',    )
                     .' ) ( . )    ,  ( ,     )   ( .
                  ). , ( .   (  ) ( , ')  .' (  ,    )
                 (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
             jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^''')
            print("You die in a fire! Game over")
        elif door_choice == "blue":
            print(r'''       _           _
                  (`-`;-"```"-;`-`)
                   \.'         './
                   /             \
                   ;   0     0   ;
                  /| =         = |\
                 ; \   '._Y_.'   / ;
                ;   `-._ \|/ _.-'   ;
               ;        `"""`        ;
               ;    `""-.   .-""`    ;
               /;  '--._ \ / _.--   ;\
              :  `.   `/|| ||\`   .'  :
               '.  '-._       _.-'   .'        jgs
               (((-'`  `"""""`   `'-)))''')
            print("Crazy hamsters crush you to death! Game over")
        elif door_choice == "yellow":
            print(r'''                         _.--.
                                    _.-'_:-'||
                                _.-'_.-::::'||
                           _.-:'_.-::::::'  ||
                         .'`-.-:::::::'     ||
                        /.'`;|:::::::'      ||_
                       ||   ||::::::'     _.;._'-._
                       ||   ||:::::'  _.-!oo @.!-._'-.
                       \'.  ||:::::.-!()oo @!()@.-'_.|
                        '.'-;|:.-'.&$@.& ()$%-'o.'\||
                          `>'-.!@%()@'@_%-'_.-o _.|'||
                           ||-._'-.@.-'_.-' _.-o  |'||
                           ||=[ '-._.-\/.-'    o |'||
                           || '-.]=|| |'|      o  |'||
                           ||      || |'|        _| ';
                           ||      || |'|    _.-'_.-'
                           |'-._   || |'|_.-'_.-'
                        jgs '-._'-.|| |' `_.-'
                                '-.||_/.-' ''')
            print("Congratulations! You found the treasure! You win!")
        elif door_choice == "run":
            print(r'''     
                 _____
              /~/~   ~\
             | |       \
             \ \        \
              \ \        \
             --\ \       .\''
            --==\ \     ,,i!!i,
                ''"'',,}{,,

            ''')
            print("You stave to death! Game over")
        else:
            print("Please enter a correct action")
    else:
        print("Please enter the correct input")

else:
    print("Please enter the correct input")




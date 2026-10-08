#intro 
import random, time
print("Welcome to shadow rps game v1.2")

print("Loading please wait")
time.sleep(4)
for i in range(4):
    load = print(i * "*")
    time.sleep(0.5)

#main menu
while True:
    gamelist = ["PLAY GAME","HOW TO PLAY", "CREDITS", "WHATS NEW?", "MORE GAMES", "QUIT"]
    for i in range(len(gamelist)):
        print(i, gamelist[i])

    print("type the number to choose your option: ")
    opt1 = int(input())

    #points and random
    pointp = 0
    pointb = 0

    gain = "Player gained a point"
    lose = "bot gained a point"
    weapons = ["r", "p", "s"]

    #MAin game loop
    if opt1 == 0:
        print("""
        LOADING PLEASE WAIT 

                        -life is a game which cannot be paused 
        """)
        time.sleep(1)
        print("The match will start in 3 seconds")
        time.sleep(1)
        for i in range(4):
            print(3 - i)
            time.sleep(1)
        
        print("welcome to the match scorers")
        time.sleep(1)
        print("""
        There will be only 15 rounds
        The player having the most points wins
        GET READY! 
        """)
        time.sleep(3)

        for i in range(14):
            choice = weapons[random.randint(0, 2)]
            
            print("Choose (r)ock, (p)aper, (s)cissors or (q)uit")
            playerc = input()

            if playerc.lower() == 'r' and choice == 's':
                pointp = pointp + 1
                print("Enemy choosed", choice)
                print("Nice move")
                print("Player +1")
            elif playerc.lower() == 'p' and choice == 'r':
                pointp = pointp + 1
                print("Enemy choosed", choice)
                print("Nice move")
                print("Player +1")
            elif playerc.lower() == 's' and choice == 'p':
                pointp = pointp + 1
                print("Enemy choosed", choice)
                print("Nice move")
                print("Player +1")
            
            elif playerc.lower() == 'r' and choice == 'p':
                pointb = pointb + 1
                print("Uh oh wrong move")
                print("Enemy choosed", choice)
                print("bot +1")
            elif playerc.lower() == 'p' and choice == 's':
                pointb = pointb + 1
                print("Uh oh wrong move")
                print("Enemy choosed", choice)
                print("bot +1")
            elif playerc.lower() == 's' and choice == 'r':
                pointb = pointb + 1
                print("Uh oh wrong move")
                print("Enemy choosed", choice)
                print("bot +1")
            
            elif playerc.lower() == 'q':
                print("Are you sure you want to quit")
                exitz = input()

                if exitz.lower() == "yes":
                    break
                else:
                    continue
            
            elif playerc.lower() == choice:
                print("Both choosed the same, it's a draw")
            else:
                print("Invalid choice 18006")
            
            
        
        print("""
        THE MATCH ENDED
        
        results""")
        print("Player = ", pointp)
        print("Enemy = ", pointb)

        if pointp > pointb:
            print("Just another victorious day, GOOD JOB!!")
            time.sleep(5)
            
        
        elif pointp < pointb:
            print("MISSION FAILED!, do not let this happen again")
            time.sleep(5)
            
         
    elif opt1 == 1:
        print("""
    What is RPS?
     
    Well RPS referres to Rock, Paper and Scissor. 
        In this game player has to choose any one, either the rock or paper or scissor
    and the other player has to do the same. While choosing both the players shouldn't
    be knowing what their enemies are choosing.

        After choosing both of the player's choices will be revealed to each other. Now 
    to decide who wins, let's take a look at the power chart
    
    COMPARISON CHART: 
    ROCK > SCISSOR        ROCK < PAPER         ROCK = ROCK 
    SCISSOR > PAPER       PAPER < SCISSOR      PAPER = PAPER
    PAPER > ROCK          SCISSOR < ROCK       SCISSOR = SCISSOR 
    
    Now the winner is declared by using the COMPARISON CHART, if palyer1 chooses rock
    and the player2 chooses paper then player2 wins and if player1 chooses scissors and 
    player2 chooses paper then player1 wins but if both choose the same it's a draw. 
    
        In this game, you'll be playing with a bot which is at medium difficulty so it
    will be match of equality and points are counted equally. To choose rock press 'r' and 
    to choose paper press 'p' and to choose scissor press 's'.
    
    ENJOY THE GAME.... 
    """)

    elif opt1 == 2:
        print("""
        CREATED BY: VISHRUTH T
        DESIGN    : VS CODES
        IDEA      : BY A PROJECT 
        """)
    elif opt1 == 3: 
        print("""
        The new update includes
    
        *MORE OPTIONS 
        *FIXED BUGS
        *IMPROVED POINTS SYSTEM
        *ADDED LOADING SCREENS
        """)
    elif opt1 == 4:
        print("More games coming soon")
    elif opt1 == 5:
        print("Are you sure?")
        ext = input()

        if ext.lower() == "yes":
            time.sleep(1)
            print("A game by shadow...")
            break
        else:
            continue





#                SHADOW RPS v1.2
#                               project approved




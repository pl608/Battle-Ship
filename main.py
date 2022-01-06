import os, socket
"""
GOING TO ADD SOCKET LATER

host = "192.0.194"
ip = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,ip))
"""

board = [[[0 for x in range(10)]] * 10]
guessmap = board
ships = {"patrol":[3,False],
         "carrier":[5,False],
         "sub":[3, False],
         "destroyer":[4, False],
         "ship":[3, False]}
alpha = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p".split(",")
def draw(outtxt: str):
    print(" |12345678910")
    print("_"*13)
    i = -1
    for x in board:
        i += 1
        print(f"{alpha[i]}|",end="")
        for y in x:
            print(f"{y}|",end="")
        print("|",end="\n")
    output = input(outtxt+ ": ")
    try: os.system("cls")
    except: os.system("clear")
    return output
name = ""
def Proccess(data):
    global name
    try:
        sdata = data.split(',')
        name = sdata[0]
        print(name)
        def check():
            global name
            name = name
            if (name in ships) == True: print(1)
            elif (name in ships) == False:
                print("The name of the ship you provided doesn't exist.\nThe available ships are:")
                for x in ships:
                    print(x)
                name = input("Please input one of the above.\nYou can only use each one once: ")
                check()
        check()
        xcoord = int(sdata[1])
        ycoord = int(sdata[2])
        orient = sdata[3]
        return name, xcoord, ycoord, orient
    except Exception as e:
        print("Your input did not work.\nPlease make sure you are using integers for the coordinates.")
        return 0,0,0,0
def Setup():
    def check():
        data = draw("ship name and placement (h for help)")
        if data == "h":
            print("""
use:
<ship-name>,<xcoord>,<ycoord>,(hor or vert for horizantal and vertical)
ALSO:
x will exit the game
""")
            data = draw("ship name and placement (h for help)")
        elif data == "x":
            import sys
            sys.exit("You told me to...")
        else:
            name, xcoord, ycoord, orient = Proccess(data)
            if name == 0:
                if xcoord == 0: check()
            if ships[name][1] == True:
                print("You already placed that ship!\nPlease try again.")
                check()
            else:
                i = 0
                print(f"{name}:{ships[name]}\n{ships[name][0]}\{ships[name][1]}")
                ships[name][1] = True
                for x in range(ships[name][0]):
                    def place():
                        try:
                            if orient == "hor":
                                if board[xcoord][ycoord+i] == 1: raise Exception('error', 'collision')
                                else: board[xcoord][ycoord+i] = 1
                            elif orient == "vert":
                                if board[xcoord][ycoord+i] == 1:
                                    
                                    raise Exception('error', 'collision')
                                else:
                                    board[xcoord+i][ycoord] = 1
                        except:
                            print("That won't work.\nThe given coordinates and orientation would place the ship out of bounds or overlap with another ship. Please try again\nby redifining the coordinates")
                            d = input("Coordinates please (e.g. 2,5): ").split(',')
            
                            xcoord = int(d[0])
                            ycoord = int(d[1])
                            place()
                    place()
    
                            
                        
                    i += 1

    for x in ships:
        check()
    input("Hit enter to start.")
    
def Guess():
    data = draw("Guess where a ship is (e.g. <x-coordinate>,<y-coordinate>): ")
    try:
        x = data.split(",")[0]
        y = data.split(",")[1]
    except:
        print("Well, you used this program incorrectly.\nInput numbers like 1, 2, 3, 4, 5, 6\nrather then one, two, three, four, five, six.")
        print("You may try again, though.")
        Guess()
    if guessmap[x][y] == 1:
        print("Well, you already tried that number. Try another one.")
        
    else:
        guessmap[x][y] = 1
    
                        
if __name__ == "__main__":
    print("Quick Note:\n     you can't play battle ship right now, because I didn't add sockets yet.\nAlso this program doesn't work well.")
    Setup()
    Guess()
     

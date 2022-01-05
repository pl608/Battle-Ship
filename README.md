# This is a Testing Branch!
so far what i added:
* a bit of networking
* a tkinter gui
* threading!
## Battle-Ship
this SHOULD work in lenux(if i spelled it wrong spam issues till I fix it) the thing that maby wont work is where it clears the screen then re-prints the battleship board along with some other stuff (to look animated)
#### Note:
the clear wont work in python idle(and if i spelled that wrong spam) because it uses os to clear because I dont know of a better way (you are free to enlighten me in issues)
## There Are Probably Tons of bug and\or error 
so just spam issues till I fix them like that
## If you want to add a ship to be used in the game you need to copy the format of the other ones

so to add a ship simply do this:
```
ships['<ship-name>'] = [<spaces>, False]]
```
spaces: int
ship-name: string (ofc)
always keep the second item in the array `False` otherwise it wont allow you to use the ship
and make sure that you do this after `ships` is defined :)
### Also I will soon add socket to make it a multiplayer game



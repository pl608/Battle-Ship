# Battle-Ship

* A fun console game in Python for bored people. Will not work in idle.
* Singleplayer for the time being, until socket functionality is added.

This SHOULD work in Linux, the thing that maybe won't work is where it clears the screen then re-prints the battleship board along with some other stuff (to look animated)
### Note:
This clearly wont work in python idle because it uses os to clear
### Adding Ships
If you want to add a ship to be used in the game you need to copy the format of the other ones, so to add a ship simply do this:
```
ships['<ship-name>'] = [<spaces>, False]]
```
```
spaces: int
ship-name: string
```
Make sure that the second item is False.

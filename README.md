# pygame_tetris
This is a custom made tetris game using only pygame code. The idea is to then train an AI to play tetris

Tetris works for the most part. I am still working out some bugs.

CONTROLS:
- W - Rotate clockwise 90 degrees
- A - Moves active piece left
- D - Moves active piece right
- S - Moves active piece down at a faster rate
- X - Clears grid(keeps score and level). IF GAME OVER, resets the game

BUGS:
- 'i' and 'j' pieces will not collide correctly when rotated by 180 degrees

- The game will crash if you rotate a piece too low to the ground(If its ending rotation goes beyong the grid size)

- You can rotate the pieces into other pieces on the grid

Future Update plans:
- Fix the 'i' and 'j' collision issues
- Pieces will be able to 'kick off' of other pieces, or not be allowed to rotate if there is no room for them. This should fix all rotation bugs, besides...
- being able to 'kick off' the floor if you rotate a tile too close to the floor
- Display next piece
- Make the UI on a seperate display layer. This will let me have more wiggle room when it comes to adding/deleting objects from the UI, and will be more optimal overall.

Update Log:
5/26/2025:

added:
- Can rotate pieces
- can clear lines
- added level progression
- added a score and level counter
- added score and level display
-   Score is added through line clear and making your piece move down at a faster rate
- add game over conditions
- added a game restart

Fixed:
- No more crashing if rotating a piece near a side wall
- Fixed collisions enough to make game playable

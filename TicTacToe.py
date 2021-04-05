# Game TIC-TAC-TOE

# Game board
game="""Tic-toc-toe        Valid Positions
   |   |             7 | 8 | 9
---+---+---         ---+---+---
   |   |             4 | 5 | 6
---+---+---         ---+---+---
   |   |             1 | 2 | 3
"""

# List of positions(horizontal and vertical)
positions = [
  None,  # Index
  (5, 1), # 1
  (5, 5), # 2
  (5, 9), # 3
  (3, 1), # 4
  (3, 5), # 5
  (3, 9), # 6
  (1, 1), # 7
  (1, 5), # 8
  (1, 9), # 9
]
# Description of the position that is winner when the game is over with row or column or diagonal
# List that contains the position that is winner

win = [
      [ 1, 2, 3], #row
      [ 4, 5, 6],
      [ 7, 8, 9],
      [ 7, 4, 1], #column
      [ 8, 5, 2],
      [ 9, 6, 3],
      [ 7, 5, 3], #diag
      [ 1, 5, 9]
    ]

board = []
for row in game.splitlines():
    board.append(list(row))

player = "X" # The player X begins
playing = True
turn = 0 # Counting the turns
while True:
    for t in board:  # Show the board
        print("".join(t))
    if not playing: # Finish when shows the last turn
        break
    if turn == 9: # If shows the turn == 9 then all positions were filled
        print("===> Sorry! Nobody won!")
        break
    position = int(input("What position do you want (1-9) (Player '%s'):" % player))
    if position < 1 or position > 9:
        print("Invalid Position! Valid 1 to 9.")
        continue
    # Check if the position is free
    if board[positions[position][0]][positions[position][1]] != " ":
        print(board[positions[position][0]][positions[position][1]])
        print("Position already used! Try another one.");
        continue
    # Update the position of the player
    board[positions[position][0]][positions[position][1]] = player
    # Check if won
    for p in win:
        for x in p:
            if board[positions[x][0]][positions[x][1]] != player:
                break
        else:
            print("\n===> The player '%s' WON (%s): "%(player, p))
            playing = False
            break
    player = "X" if player == "O" else "O" # Update the player
    turn += 1 # Next turn
    
print("\nGame OVER!")
# Tic Tac Toe game with keyboard emoji characters using Python

board = {
'1️⃣': ' ', '2️⃣': ' ', '3️⃣': ' ',
'4️⃣': ' ', '5️⃣': ' ', '6️⃣': ' ',
'7️⃣': ' ', '8️⃣': ' ', '9️⃣': ' '
}

def print_board(board):
print(board['1️⃣'] + '|' + board['2️⃣'] + '|' + board['3️⃣'])
print('-+-+-')
print(board['4️⃣'] + '|' + board['5️⃣'] + '|' + board['6️⃣'])
print('-+-+-')
print(board['7️⃣'] + '|' + board['8️⃣'] + '|' + board['9️⃣'])

def check_winner(board, player):
if (board['1️⃣'] == player and board['2️⃣'] == player and board['3️⃣'] == player) or \
(board['4️⃣'] == player and board['5️⃣'] == player and board['6️⃣'] == player) or \
(board['7️⃣'] == player and board['8️⃣'] == player and board['9️⃣'] == player) or \
(board['1️⃣'] == player and board['4️⃣'] == player and board['7️⃣'] == player) or \
(board['2️⃣'] == player and board['5️⃣'] == player and board['8️⃣'] == player) or \
(board['3️⃣'] == player and board['6️⃣'] == player and board['9️⃣'] == player) or \
(board['1️⃣'] == player and board['5️⃣'] == player and board['9️⃣'] == player) or \
(board['3️⃣'] == player and board['5️⃣'] == player and board['7️⃣'] == player):
return True
else:
return False

def is_board_full(board):
for key in board.keys():
if board[key] == ' ':
return False
return True

print_board(board)
player = '✅'
number_of_turns = 0
game_over = False

while not game_over:
move = input("It's your turn," + player + ". Choose a spot 1-9: ")
if board[move] == ' ':
board[move] = player
number_of_turns += 1
print_board(board)
if check_winner(board, player):
print(player + ' won!')
game_over = True
elif is_board_full(board):
print("It's a tie!")
game_over = True
else:
if player == '✅':
player = '❎'
else:
player = '✅'
else:
print("That spot is already taken. Please choose again.")

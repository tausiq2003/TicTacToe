from random import choice

class Player():
    def __init__(self, symbol, name):
        self._symbol = symbol
        self._name = name

    @property
    def symbol(self):
        return self._symbol

    @property
    def name(self):
        return self._name

class Board():
    def __init__(self):
        self._board = [["" for j in range(3)] for i in range(3)]

    @property
    def board(self):
        return self._board

class Move():
    def __init__(self, player, row, col):
        self._player = player
        self._row = row
        self._col = col

    @property
    def player(self):
        return self._player

    @property
    def row(self):
        return self._row

    @property
    def col(self):
        return self._col

def checkWinner(board, symbol):
    for i in range(3):
        if board[i][0] == symbol and board[i][1] == symbol and board[i][2] == symbol:
            return True
        elif board[0][i] == symbol and board[1][i] == symbol and board[2][i] == symbol:
            return True
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return True
    elif board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return True
    return False

def checkDraw(board, checkWinner):
    if checkWinner(board, "X") or checkWinner(board, "O"):
        return False
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                return False
    return True

def isGameOver(board, checkWinner):
    return checkWinner(board, "X") or checkWinner(board, "O") or checkDraw(board, checkWinner)
def getWinner(board, checkWinner, player1, player2):
    if checkWinner(board, player1.symbol):
        return player1
    elif checkWinner(board, player2.symbol):
        return player2
    else:
        return None

def makeMove(board, move):
    board[move.row][move.col] = move.player.symbol

def getValidMoves(board, current_player):
    valid_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                valid_moves.append(Move(current_player, i, j))
    return valid_moves

def main():
    player1 = Player(choice(["X", "O"]), "Player 1")
    player2 = Player("X" if player1.symbol == "O" else "O", "Player 2")
    board = Board()


    print(board.board)
    players = [player1, player2]

    print(player1.symbol, player2.symbol)
    current_player = players[0]

    while not isGameOver(board.board, checkWinner):
        valid_moves = getValidMoves(board.board, current_player)

        #this is for random moves. 
        current_player.move = choice(valid_moves)
        #not useful in gui but useful for random moves
        makeMove(board.board, current_player.move)

        # this is for testing purposes
        for row in board.board:
            print(row)

        print()

        if isGameOver(board.board, checkWinner):
            break

        # Took little help here. if 1 then 0 if 0 then 1
        current_player = players[(players.index(current_player) + 1) % 2]

    winner = getWinner(board.board, checkWinner, player1, player2)
    if winner:
        print(f"{winner.name} ({winner.symbol}) wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
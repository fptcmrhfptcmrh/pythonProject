# 구현해야 하는 함수들

def initializeBoard():
    gameBoard = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    return gameBoard


def printBoard(gameBoard):
    print("\n====== BOARD ======\n")
    print("      ", end="")
    for i in range(3):
        print("B=%d " % (i + 1), end="")
    print("\n")
    for i in range(3):
        print(" A=%d   " % (i + 1), end="")
        ithLine = gameBoard[i]
        for i in range(3):
            print(ithLine[i], "  ", end="")
        print("\n")
    print("===================\n")


def inputAB(currentPlayer):
    print(currentPlayer)
    a,b=input("A=?  B=?").split()
    return int(a),int(b)

def isRightRange(A, B):
    if 1<=A and A<=3 and 1<=B and B<=3:
        return True
    else:
        return False

def getABonBoard(A, B):
    A-=1
    B-=1
    return A,B

def isEmptyCell(gameBoard, A, B):
    if gameBoard[A][B]=='.':
        return True
    else:
        return False

def updateBoard(gameBoard, A, B, mark):
    gameBoard[A][B]=mark

def getNextPlayer(player):
    if player=='x':
        return 'o'
    elif player=='o':
        return 'x'


def isBingoInA(gameBoard):
    for i in range(0,3):
        if gameBoard[i][0]==gameBoard[i][1]:
            if gameBoard[i][1]==gameBoard[i][2]:
                if gameBoard[i][0]==gameBoard[i][2]:
                    if gameBoard[i][2]!='.':
                        return True
    return False

def isBingoInB(gameBoard):
    for i in range(0,3):
        if gameBoard[0][i]==gameBoard[1][i]:
            if gameBoard[1][i]==gameBoard[2][i]:
                if gameBoard[0][i]==gameBoard[2][i]:
                    if gameBoard[2][i] != '.':
                        return True
    return False

def isBingoInDiagonal(gameBoard):
    if gameBoard[0][0]==gameBoard[1][1]:
        if gameBoard[1][1]==gameBoard[2][2]:
            if gameBoard[2][2] != '.':
                return True
    if gameBoard[0][2]==gameBoard[1][1]:
        if gameBoard[1][1]==gameBoard[2][0]:
            if gameBoard[2][0] != '.':
                return True
    return False

def isBingo(gameBoard):
    return isBingoInA(gameBoard) or isBingoInB(gameBoard) or isBingoInDiagonal(gameBoard)

def isFull(gameBoard):
    for i in range(0,2):
        for j in range(0,2):
            if gameBoard[i][j]=='.':
                return False
    return True

startPlayer = 'x'

isEndOfGame = False
gameBoard = initializeBoard()
player = startPlayer

while not isEndOfGame:
    printBoard(gameBoard)
    inputA, inputB = inputAB(player)

    if isRightRange(inputA, inputB):
        A, B = getABonBoard(inputA, inputB)

        if isEmptyCell(gameBoard, A, B):
            updateBoard(gameBoard, A, B, player)

            if isBingo(gameBoard):
                printBoard(gameBoard)
                print("축하합니다!!! 승자는: %s 입니다." % player)
                isEndOfGame = True
            elif isFull(gameBoard):
                printBoard(gameBoard)
                print("보드판이 다 찼습니다. 숫자를 다시 입력해주세요.")
                isEndOfGame = True
            else:
                player = getNextPlayer(player)

        else:
            print("이미 채워진 칸입니다. 숫자를 다시 입력해주세요.")

    else:
        print("범위를 벗어난 숫자를 선택하였습니다. 숫자를 다시 입력해주세요.")


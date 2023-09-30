from copy import deepcopy
import pygame

RED = (255,0,0)
WHITE = (255,255,255)

def minimax(position, depth, maxPlayer, game):
    pass
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
    if maxPlayer :
        maxEval = float('-inf')
        my_move = None
        for move in getAllMoves(position, WHITE, game):
            evaluation = minimax(move, depth-1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                my_move = move
        
        return maxEval, my_move
    else:
        minEval = float('inf')
        my_move = None
        for move in getAllMoves(position, RED, game):
            evaluation = minimax(move, depth-1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                my_move = move
        
        return minEval, my_move


def simulateMove(piece, move, board, game, skip):
    pass
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)
    return board

def getAllMoves(board, color, game):
    pass
    moves = []
    for piece in board.getAllPieces(color):
        gvm = board.getValidMoves(piece)
        for move, skip in gvm.items():
            temp_b = deepcopy(board)
            temp_p = temp_b.getPiece(piece.row, piece.col)
            new_b = simulateMove(temp_p, move, temp_b, game, skip)
            moves.append(new_b)
    return moves
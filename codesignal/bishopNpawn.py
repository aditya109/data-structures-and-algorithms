"""Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited to diagonal movement

For bishop = "a1" and pawn = "c3", the output should be
bishopAndPawn(bishop, pawn) = true

For bishop = "h1" and pawn = "h3", the output should be
bishopAndPawn(bishop, pawn) = false.
"""
def bishopAndPawn(bishop, pawn):
    bishop_x = ord(bishop[0])-97
    bishop_y = ord(bishop[1])-49
    
    pawn_x = ord(pawn[0])-97
    pawn_y = ord(pawn[1])-49

    print((bishop_x, bishop_y), (pawn_x, pawn_y))
    return(abs(bishop_x - pawn_x) == abs( bishop_y - pawn_y))

print(bishopAndPawn("a5", "c3"))



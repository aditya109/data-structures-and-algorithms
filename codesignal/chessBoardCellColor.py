def chessBoardCellColor(cell1, cell2):
    rowOfCell1 = ord(cell1[0])%65
    columnOfCell1 = int(cell1[1]) - 1
    rowOfCell2 = ord(cell2[0])%65
    columnOfCell2 = int(cell2[1]) - 1

    return (rowOfCell1+columnOfCell1) % 2 == (rowOfCell2+columnOfCell2) %2   

print(chessBoardCellColor(cell1 = "A1", cell2 = "H3"))
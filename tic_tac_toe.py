box=[['_','_','_'],
     ['_','_','_'],
     ['_','_','_']]
def win_logic():
    for row in box:
        all_cells_match = True
        for cell in row:
            if cell != tool:
                all_cells_match = False
                break
        if all_cells_match:
            return True

    for j in range(3):
        all_cells_match = True
        for i in range(3):
            if box[i][j] != tool:
                all_cells_match = False
                break
        if all_cells_match:
            return True

    for i in range(3):
        if box[i][2 - i] != tool:
            break
    else:
        return True

    for i in range(3):
        if box[i][i] != tool:
            break
    else:
        return True

    return False

    #DIAGONAL WIN LOGIC FROM TOP LEFT
    for i in range(3):
        if box[i][i] != tool:
            print('')
        else:
            print('winner')
n=0
toolno=0
while True:
    if n>=9 and toolno>=9:
        break
    row=int(input("enter the row: "))
    column=int(input("enter the column: "))
    if toolno%2==0:
        tool='x'
    else:
        tool='o'
    if 1 <= row <= 3 and 1 <= column <= 3:
        if box[row-1][column-1] == '_':
            box[row-1][column-1]=tool
            print(box)
        else:
            print('Already played')
    else:
        print('enter numbers below 3')
    if win_logic():
        print(f"Player {tool} wins!")
        break   
    toolno=toolno+1
    n=n+1



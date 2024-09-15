box=[['_','_','_'],
     ['_','_','_'],
     ['_','_','_']]
def win_logic():
    for row in box:
        if all(cell==tool for cell in row):
            print("winner")
            return True
    for col in range(3):
        if all(box[row][col] == tool for row in range(3)):
            print(f"Player {tool} wins on a column!")
            return True
    if all(box[i][i] == tool for i in range(3)):
        print(f"Player {tool} wins on the main diagonal!")
        return True
    if all(box[i][2 - i] == tool for i in range(3)):
        print(f"Player {tool} wins on the anti-diagonal!")
        return True

    return False
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
    if win_logic(tool):
        break   
    toolno=toolno+1
    n=n+1



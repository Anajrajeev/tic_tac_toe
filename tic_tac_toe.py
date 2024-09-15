box=[['_','_','_'],
     ['_','_','_'],
     ['_','_','_']]
n=0
toolno=0
while True:
    if n>=9 and tool>=9:
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
        
    toolno=toolno+1
    n=n+1

def win_logic():
    for i in box:
        for j in box:
            
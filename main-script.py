canvas_x=5
canvas_y=5
x=0
y=0
directions=['WEST','SOUTH','EAST','NORTH']
direction='NORTH'
menuNo=0
dirIndex=0

def report(): 
    state = "Current state is: ({}, {}, {})"
    print('\n\n'+ state.format(x,y,direction)+ '\n\n')

def showMenu():
    print('\n\nThis is a 5*5 area,the robot is headed to north located at (0,0) position by default.')
    print('Please choose a number from menu, if this is your first entry choose PLACE first:')
    print('1.PLACE'+'\n'+'2.MOVE'+'\n'+'3.LEFT'+'\n'+'4.RIGHT'+'\n'+'5.REPORT'+'\n'+'6.EXIT')

def numberValid():
    while True:
        try:
            num = input("Please enter a number: ")
            val=int(num)
            break
        except ValueError:
            print('oops! '+ num +' is not a valid number,try again')
    return val

def getx():
    # get x value from user
    print('Choose an integer number for x location (0-5):')
    user_x=numberValid()
    while(user_x>5 or user_x<0):
        print('Error,Please enter a correct number!')
        print('Choose an integer number for x location (0-5):')
        user_x=numberValid()
    global x
    x=user_x

def gety():
    # get y value from user
    print('\n\n Choose an integer number for Y location (0-5):')
    user_y=numberValid()
    while(user_y>5 or user_y<0):
        print('\n\n Error,Please enter a correct number!')
        print('\n Choose an integer number for Y location (0-5):')
        user_y=numberValid()
    global y
    y=user_y

def getDirection():
    global dirIndex
    state = "Please choose your direction:\n \t\t\t 1.{}\n \t\t\t 2.{}\n \t\t\t 3.{}\n \t\t\t 4.{}"
    print(state.format(directions[0],directions[1],directions[2],directions[3]))  
    dirIndex=numberValid()-1
    while(dirIndex>3 or dirIndex<0):
        # check that user selects one of valid directions
        print('Error,Please enter a correct number!')
        print(state.format(directions[0],directions[1],directions[2],directions[3]))
        dirIndex=numberValid()-1
    #find the value for the direction in the dictionary
    global direction
  
    direction=directions[dirIndex]
    return dirIndex

def move():
    global y
    global x
    if(direction=='NORTH' and y<canvas_y):
        y+=1
        
    elif(direction=='SOUTH' and y<canvas_y and y>0):
        y-=1
        
    elif(direction=='WEST' and x<canvas_x):
        x+=1
        
    elif(direction == 'EAST' and x<canvas_x and x>0):
        x-=1

def rightRot():
    # The robot rotates 90 degrees to right 
    global dirIndex
    try:
        #check array out of bound
        if(dirIndex==len(directions)):
            dirIndex==0
        else:
            dirIndex+=1
    except:
        print('error!')

    global direction
    direction=directions[dirIndex]

def leftRot():
    # The robot rotates 90 degrees to left
    global dirIndex
    try:
        #check array out of bound
        if(dirIndex==0):
            dirIndex=len(directions)-1
        else:
            dirIndex-=1
    except:
        print('error!')

    global direction
    direction=directions[dirIndex]
 
def startGame():
    showMenu()
    global menuNo
    menuNo=numberValid()
    while(menuNo !=6):
        # if user didn't choose to exit do: 
        if menuNo==1:
            #user chooses PLACE function (x,y,direction)
            getx()
            gety()
            getDirection()
        if menuNo==2:
            #robot goes one step forward through either x or y axis
            move()
        if menuNo==3:
            leftRot()
        if menuNo==4:
            rightRot()
        if(menuNo==5):
            # gives the latest state of the robot
            report()

        showMenu()
        menuNo=numberValid()

    print('You chose to exit!')


startGame()





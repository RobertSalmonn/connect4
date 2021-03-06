import turtle

wn=turtle.Screen()
wn.tracer(0)
wn.bgcolor("blue")
wn.setup(width=600, height=600)

game_over="no"
turn="yellow"
counter=0

v_turn=1
board=[[0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1]]



p_pen=turtle.Turtle()
p_pen.penup()
p_pen.color("white")
p_pen.goto(0, -260)
p_pen.hideturtle()


g_pen=turtle.Turtle()
g_pen.penup()
g_pen.color("white")
g_pen.goto(0, 200)
g_pen.hideturtle()

pen=turtle.Turtle()
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(-210, 180)
pen.pendown()
##pen.hideturtle()
for i in range (2):
    pen.forward(420)
    pen.right(90)
    pen.forward(360)
    pen.right(90)
for i in range (7):
    pen.forward(60)
    pen.right(90)
    pen.forward(360)
    pen.right(180)
    pen.forward(360)
    pen.right(90)

pieces=[]
class Piece (turtle.Turtle):
    def __init__(self):
        
        global turn
        global v_turn
        
        if turn=="red":
            turn="yellow"
            v_turn=2
        elif turn=="yellow":
            turn="red"
            v_turn=1


        
        
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("circle")
        if turn=="red":
            self.color("red")
        else:
            self.color("yellow")
        self.speed(0)
        self.shapesize(stretch_wid=2, stretch_len=2)
        pieces.append(self)

    def animate (self):
        global game_over
        
        
        y=self.ycor()
        for i in range (6):
            if board[i+1][column]==1 or board[i+1][column]==2:
                if turn=="red":
                    board[i][column]=1

                elif turn=="yellow":
                    board[i][column]=2
                    
                
                break
                
            else:
                y-=60
                self.sety(y)

        if counter==42:
            game_over="yes"
            
            tie()

        
        for i in range (4):
            for j in range (6):
                if board[j][i]==v_turn and board[j][i+1]==v_turn and board[j][i+2]==v_turn and board[j][i+3]==v_turn:
                    game_over="yes"
                    
                    
                    win(turn)

        for i in range (7):
            for j in range (3):
                if board[j][i]==v_turn and board[j+1][i]==v_turn and board[j+2][i]==v_turn and board[j+3][i]==v_turn:
                    game_over="yes"
                    win(turn)
        for i in range (4):
            for j in range (3):
                if board[j][i]==v_turn and board[j+1][i+1]==v_turn and board[j+2][i+2]==v_turn and board[j+3][i+3]==v_turn:
                    game_over="yes"

                    win(turn)

        for i in range (3, 7):
            for j in range (3):
                if board[j][i]==v_turn and board[j+1][i-1]==v_turn and board[j+2][i-2]==v_turn and board[j+3][i-3]==v_turn:
                    game_over="yes"
                    win(turn)
        
                    

                
                
   
            

        
        


p_pen.write(f"red's go", align="center", font=("Calibri", 30))
def dropzone(x, y):
    global game_over
    global turn
    global counter
    global column
    global fail
    global counter




    
    if game_over=="no":
        
        piece=Piece()

        
        
        if x>-210 and x<-150 and board[0][0]==0:
            piece.goto(-180, 150)
            column=0
            counter+=1
            piece.animate()
        elif x>-150 and x<-90 and board[0][1]==0:
            piece.goto(-120, 150)
            column=1
            counter+=1
            piece.animate()
        elif x>-90 and x<-30 and board[0][2]==0:
            piece.goto(-60, 150)
            column=2
            counter+=1
            piece.animate()
        elif x>-30 and x<30 and board[0][3]==0:
            piece.goto(0, 150)
            column=3
            counter+=1
            piece.animate()
        elif x>30 and x<90 and board[0][4]==0:
            piece.goto(60, 150)
            column=4
            counter+=1
            piece.animate()
        elif x>90 and x<150 and board[0][5]==0:
            piece.goto(120, 150)
            column=5
            counter+=1
            piece.animate()
        elif x>150 and x<210 and board[0][6]==0:
            piece.goto(180, 150)
            column=6
            counter+=1
            piece.animate()
            

        else:
            piece.goto(1000, 1000)
            if turn=="red":
                turn="yellow"
            else:
                turn="red"

        if turn=="red":
            turn="yellow"
        else:
            turn="red"
            

        p_pen.clear()
        p_pen.write(f"{turn}'s go", align="center", font=("Calibri", 30))
        if turn=="red":
            turn="yellow"
        else:
            turn="red"
        print (counter)
    else:
        pass

        

        
    
    



        
    


def win(team):
    pen.penup()
    pen.goto(0,200)
    g_pen.write(f"{team} wins!", align="center", font=("Calibri", 50))
    

def tie():
    pen.penup()
    pen.goto(0,200)
    g_pen.write(f"Draw!", align="center", font=("Calibri", 50))

    
def replay():
    global turn
    global game_over
    global counter
    counter=0
    game_over="no"
    turn="yellow"
    p_pen.clear()
    p_pen.write(f"red's go", align="center", font=("Calibri", 30))
    g_pen.clear()
    
    for i in range (6):
        for j in range (7):
            if board[i][j]!=0:
                board[i][j]=0

    for piece in pieces:
        piece.goto(1000, 1000)
    



wn.listen()
wn.onscreenclick(dropzone)
wn.onkeypress(replay, "r")



while True:
    wn.update()
    
    

import turtle

wn=turtle.Screen()
wn.tracer(0)
wn.bgcolor("blue")
wn.setup(width=600, height=600)

turn="yellow"
v_turn=1
board=[[0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1]]




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

        
        for i in range (4):
            for j in range (6):
                if board[j][i]==v_turn and board[j][i+1]==v_turn and board[j][i+2]==v_turn and board[j][i+3]==v_turn:
                    
                    win(turn)

        for i in range (7):
            for j in range (3):
                if board[j][i]==v_turn and board[j+1][i]==v_turn and board[j+2][i]==v_turn and board[j+3][i]==v_turn:
                    
                    win(turn)
        for i in range (4):
            for j in range (3):
                if board[j][i]==v_turn and board[j+1][i+1]==v_turn and board[j+2][i+2]==v_turn and board[j+3][i+3]==v_turn:
                    
                    win(turn)

        for i in range (3, 7):
            for j in range (3):
                if board[j][i]==v_turn and board[j+1][i-1]==v_turn and board[j+2][i-2]==v_turn and board[j+3][i-3]==v_turn:
                    
                    win(turn)
                    

                
                
   
            

        
        



def dropzone(x, y):
    
    global column
    piece=Piece()
    
    if x>-210 and x<-150:
        piece.goto(-180, 150)
        column=0
    elif x>-150 and x<-90:
        piece.goto(-120, 150)
        column=1
    elif x>-90 and x<-30:
        piece.goto(-60, 150)
        column=2
    elif x>-30 and x<30:
        piece.goto(0, 150)
        column=3
    elif x>30 and x<90:
        piece.goto(60, 150)
        column=4
    elif x>90 and x<150:
        piece.goto(120, 150)
        column=5
    elif x>150 and x<210:
        piece.goto(180, 150)
        column=6
    piece.animate()
    


wn.listen()
wn.onscreenclick(dropzone)
        
    


def win(team):
    pen.penup()
    pen.goto(0,200)
    pen.write(f"{team} wins!", align="center", font=("Calibri", 50))
    








while True:
    wn.update()
    
    

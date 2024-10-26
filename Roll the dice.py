

from turtle import RawTurtle, TurtleScreen
import random
import tkinter as tk
from tkinter import font


god = tk.Tk()
god.maxsize(width=1000, height=600)
god.title('Roll The Dice (3D)')

font = font.Font(family='Elephant', size= 18)

frame = tk.Frame(master=god,  padx=20,pady=20)
frame.pack(side='left')
canvas = tk.Canvas(master=god, width=600, height=500)
canvas.pack(side='right')
fram = TurtleScreen(canvas)
die_outline=RawTurtle(fram)



die_outline.hideturtle()
die_outline.penup()
die_outline.speed(5)
die_outline.pensize(10)

def draw_dice_outline():
    die_outline.hideturtle()
    die_outline.clear()
    die_outline.goto(-100, 100)  
    die_outline.pendown()
    die_outline.fillcolor('white')
    die_outline.begin_fill()

    die_outline.goto(100, 100)
    die_outline.goto(100, -100)
    die_outline.goto(-100, -100)
    die_outline.goto(-100, 100)
    die_outline.end_fill()

    die_outline.fillcolor('gray90')
    die_outline.begin_fill()
    die_outline.goto(50, 150)
    die_outline.goto(250, 150)
    die_outline.goto(250, -50)
    die_outline.goto(100, -100)
    die_outline.goto(100, 100)
    die_outline.goto(50, 150)
    die_outline.end_fill()

    die_outline.fillcolor('gray80')
    die_outline.begin_fill()
    die_outline.goto(-100, 100)
    die_outline.goto(50, 150)
    die_outline.goto(250, 150)
    die_outline.goto(100, 100)
    die_outline.goto(-100, 100)
    die_outline.end_fill()

    die_outline.penup()
draw_dice_outline()

dot_positions_3d = {
    1: [((0, 0), 'black')],  
    2: [((-50, 50), 'black'), ((50, -50), 'black')],
    3: [((-50, 50), 'black'), ((0, 0), 'black'), ((50, -50), 'black')], 
    4: [((-50, 50), 'black'), ((50, 50), 'black'), ((-50, -50), 'black'), ((50, -50), 'black')],
    5: [((-50, 50), 'black'), ((50, 50), 'black'), ((0, 0), 'black'), ((-50, -50), 'black'), ((50, -50), 'black')], 
    6: [((-50, 50), 'black'), ((50, 50), 'black'), ((-50, 0), 'black'), ((50, 0), 'black'), ((-50, -50), 'black'), ((50, -50), 'black')]
}

dot = []
for _ in range(7):
    die_outline = RawTurtle(fram)
    die_outline.shape('circle')
    die_outline.penup()
    die_outline.hideturtle()
    dot.append(die_outline)

hist = []
def click():
    num = random.randint(1, 6)
    roll = tk.Label(master=frame, text= (f"Rolled a {num}" ), font=font)
    roll.grid(row=3,column=0)
    hist.append(num)
   
    for die_outline in dot:
        die_outline.hideturtle()

    for i, (pos, color) in enumerate(dot_positions_3d[num]):
        dot[i].goto(pos)
        dot[i].color(color)
        dot[i].showturtle()

def history():
    win = tk.Tk()
    win.title('History')
    hist_l = tk.Label(master=win, text=(f"Your history: {hist}"))
    hist_l.pack()
    



start= tk.Button(master=frame, text='Roll',command= click, font= font)
start.grid(row=1,column=0)
hist0 = tk.Button(master=frame, text='History', command= history)
hist0.grid(row=5,column=0)


god.mainloop()

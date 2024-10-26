import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkfont

# Creating the main root
root1 = tk.Tk()
root1.maxsize(width=500,height=500)

root1.title('Tic Tac Toe (by sss.)')
font= tkfont.Font(family= 'Comic Sans MS', size= 15, )


current_player = '❌'
winner = None



def play():
    root1.destroy()
    root = tk.Tk()
    root.maxsize(width=500,height=500)
    root.title('Tic Tac Toe (by sss.)')

    
    board = [["" for _ in range(3)] for _ in range(3)]
    buttons = [[None for _ in range(3)] for _ in range(3)]
    def replay():
        global current_player, winner
        current_player = "❌"
        winner = None
        for r in range(3):
            for c in range(3):
                board[r][c] = ""
                buttons[r][c].config(text="")
        
    def check_winner():
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != "":
                return board[i][0]
            if board[0][i] == board[1][i] == board[2][i] != "":
                return board[0][i]
        if board[0][0] == board[1][1] == board[2][2] != "":
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != "":
            return board[0][2]
        return None

    def on_button_click(r, c):
        global current_player, winner
        if board[r][c] == "" and not winner:
            board[r][c] = current_player
            buttons[r][c].config(text=current_player)
            winner = check_winner()
            if winner:
                messagebox.showinfo("Game Over",f"Player {winner} wins!",)
                list1= []
                list1.append(winner)
                        
            elif all(cell != "" for row in board for cell in row):
                messagebox.showinfo("Game Over", "It's a draw!")
                            
            else:
                current_player = "⭕" if current_player == "❌" else "❌"
    
    for r in range(3):
        for c in range(3):
            buttons[r][c] = tk.Button(master= root, text="", width=10, height=3, command=lambda r=r, c=c: on_button_click(r, c), font=font ,cursor='hand2',activebackground='green')
            buttons[r][c].grid(row=r, column=c)
    replay_b= tk.Button(master=root, text= '| Replay |', font=font, command= replay)
    replay_b.grid (row= 4, column = 1, pady= 5 )

    
    root.mainloop()
    


text_play= tk.Label(master=root1, text=' Press the button below to play!!', font=font)
text_play.grid(row= 2, column=2, pady= 5, padx=10)
button_play = tk.Button(master=root1 ,text='Play', width=5, command= play,cursor='hand2')
button_play.grid(row= 3, column=2, pady= 5, padx=5)




root1.mainloop()

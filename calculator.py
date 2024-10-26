# Importing all functions-----------------------------------------------------------------------------------------------
import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN
import tkinter.font as tkfont

# Creating functions of Main root------------------------------------------------------------------------------

# Creating the main root
root = tk.Tk()
root.maxsize(width=800,height=285)
root.minsize(width= 525, height=265)
root.title('Simple Calculator (by sss.)')

# Creating the working area
frame = tk.Frame(master=root, bg="black", padx=20,pady=20,)
frame.pack()

# Importing font settings
font= tkfont.Font(family= 'Comic Sans MS', size= 15, )
font2= tkfont.Font(family='Lucida Sans Typewriter', size=14)

# Creating the index
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=0, width=30,cursor='tcross',font=font , justify= 'right', selectbackground='light green',selectforeground='blue',)
entry.grid(row=0, column=0, columnspan=5, ipady=3,ipadx=5, pady=5)

#defining new functions------------------------------------------------------------------------------------------------------

#defining functions of buttons
def myclick(number):
    entry.insert(tk.END, number)



#defing font settings   
def increase_font_size():
    max_magnification= 26
    size1= (font.actual()['size'] )
    font.config(size=size1)
    if size1 < max_magnification:
        size1= (font.actual()['size']+1)
        font.config(size=size1)
    else:
        tkinter.messagebox.showinfo('Error!',"Maximum Size Reached!!")
def decrease_font_size():
    min_magnification= 10
    size2= (font.actual()['size'])
    font.config(size= size2)
    if size2 > min_magnification:
        size2= (font.actual()['size']-1)
        font.config(size=size2)
    else:
        tkinter.messagebox.showinfo('Error!',"Minimum Size Reached!!")

# Function to update the display
def update_display(value):
    current = entry.get()
    entry.delete(0,tk.END)
    entry.insert(0, current + value)
    

# Function to toggle positive/negative
def toggle_sign():
    current = entry.get()
    if current.startswith('-'):
        entry.delete(0)
    else:
        entry.insert(0, '-')
    
# Function to calculate percentage
def percentage():
    try:
        current = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, (current / 100))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# defining funtion of equal button
def equal():
    try:
        y = (eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
# defining function of clear button
def clear():
    entry.delete(0, tk.END)

# Function to backspace
def backspace():
    current = entry.get()
    entry.delete(len(current) - 1, tk.END)


# Creating and Arranging buttons-------------------------------------------------------------------------------------------

# Creating magnification button
button_sizeplus= tk.Button(master=frame, text='🔍+', padx=1,pady=1, width=4, command=increase_font_size, border=5)
button_sizeplus.grid(row=0, column=6, pady= 2,padx=0)
button_sizeminus= tk.Button(master=frame, text='🔍-', padx=1,pady=1, width=4, command=decrease_font_size, border= 5)
button_sizeminus.grid(row=0,column= 5, pady=2)

# Creating no. 0 to 9
button_1 = tk.Button(master=frame, text='1', padx=15,pady=5, width=3, command=lambda: myclick(1),font=font2)
button_1.grid(row=1, column=0, pady=2)
button_2 = tk.Button(master=frame, text='2', padx=15, pady=5, width=3, command=lambda: myclick(2),font=font2)
button_2.grid(row=1, column=1, pady=2)
button_3 = tk.Button(master=frame, text='3', padx=15, pady=5, width=3, command=lambda: myclick(3),font=font2)
button_3.grid(row=1, column=2, pady=2)
button_4 = tk.Button(master=frame, text='4', padx=15, pady=5, width=3, command=lambda: myclick(4),font=font2)
button_4.grid(row=2, column=0, pady=2)
button_5 = tk.Button(master=frame, text='5', padx=15, pady=5, width=3, command=lambda: myclick(5),font=font2)
button_5.grid(row=2, column=1, pady=2)
button_6 = tk.Button(master=frame, text='6', padx=15,pady=5, width=3, command=lambda: myclick(6),font=font2)
button_6.grid(row=2, column=2, pady=2)
button_7 = tk.Button(master=frame, text='7', padx=15,pady=5, width=3, command=lambda: myclick(7),font=font2)
button_7.grid(row=3, column=0, pady=2)
button_8 = tk.Button(master=frame, text='8', padx=15,pady=5, width=3, command=lambda: myclick(8),font=font2)
button_8.grid(row=3, column=1, pady=2)
button_9 = tk.Button(master=frame, text='9', padx=15,pady=5, width=3, command=lambda: myclick(9),font=font2)
button_9.grid(row=3, column=2, pady=2)
button_0 = tk.Button(master=frame, text='0', padx=15,pady=5, width=3, command=lambda: myclick(0),font=font2)
button_0.grid(row=4, column=1, pady=2)

# Creating bracket buttons
button_openbracket = tk.Button(master=frame, text='(' , padx=15, pady= 5, width=1 , command= lambda: myclick('('),font=font2)
button_openbracket.grid(row=2, column=3 , pady= 1)
button_closebracket = tk.Button(master=frame, text=')' , padx=15, pady= 5, width= 1, command= lambda: myclick(')'),font=font2)
button_closebracket.grid(row=3, column=3 , pady= 2)

# Creating +/- button
button_negativepositive = tk.Button(master=frame, text='+/-', padx=15,pady= 5, width= 3, command= toggle_sign,font=font2)
button_negativepositive.grid(row = 4, column=2, pady=2)

# Creating dot button
button_dot = tk.Button(master= frame, text='.', padx= 15, pady=5, width=3, command=lambda: myclick('.'),font=font2)
button_dot.grid(row = 4, column=0, pady=2)

# Creating buttons of all arithmetic functions
button_per= tk.Button(master=frame, text="%", padx=15,pady=5, width=2, command=percentage,bg='grey', fg='white',font=font2)
button_per.grid(row= 4, column=3, pady= 2)

button_add = tk.Button(master=frame, text="+", padx=15,pady=5, width=2, command=lambda: myclick('+'),bg='grey', fg='white',font=font2)
button_add.grid(row=1, column=4, pady=2)

button_subtract = tk.Button(master=frame, text="-", padx=15, pady=5, width=2, command=lambda: myclick('-'),bg='grey', fg='white',font=font2)
button_subtract.grid(row=2, column=4, pady=2)

button_multiply = tk.Button(master=frame, text="x", padx=15, pady=5, width=2, command=lambda: myclick('*'),bg='grey', fg='white',font=font2)
button_multiply.grid(row=3, column=4, pady=2)

button_div = tk.Button(master=frame, text="÷", padx=15, pady=5, width=2, command=lambda: myclick('/'),bg='grey', fg='white',font=font2)
button_div.grid(row=4, column=4, pady=2)

button_backspace = tk.Button(master=frame, text='⌫', padx=15, pady=5, width=1, command= backspace, bg= 'red', fg= 'white')
button_backspace.grid(row=1, column=3, pady=2)

# Creating clear and equal buttons
button_clear = tk.Button(master=frame, text="clear",padx=15, pady=5, width=3, command=clear, bg= 'Red', fg= 'white',font=font2)
button_clear.grid(row=1, column=5,  pady=2)

button_equal = tk.Button(master=frame, text="=", padx=15, pady=5, width=3, command=equal, height=6, bg="light green",font=font2)
button_equal.grid(row=2, column=5,  pady=2, rowspan=4)

# Runing the program
root.mainloop()
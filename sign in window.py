import tkinter as tk

win = tk.Tk()
win.title("Sign in window")
win.geometry("300x200")
win.resizable(False, False)


# defing the function-----------------------------------------------------------
file_name = "document_new_created_saved_data.txt"
content = 'A storage place is created-------------------------\n'
def load_data():
    try:
        with open(file_name, "r") as file:
            data = file.read().strip().split("\n")
            return data
    except FileNotFoundError:
        try:
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"File '{file_name}' created successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")
            

def already_sign():
    canvas_2 = tk.Canvas(win, height=500, width=300)
    canvas_2.place(x=0, y=0)
    label_n = tk.Label(canvas_2, text="Old user window", font=("Arial", 20),anchor="center")
    label_n.grid(row=0, column=1,columnspan=2)  
    user_name = tk.Label(canvas_2, text="User name:", font=("Arial", 15),anchor="center")
    user_name.grid (row=3, column=1,ipady=5)
    user_name_entry = tk.Entry(canvas_2, font=("Arial", 10),justify='left',width=30)
    user_name_entry.grid(row=3, column=2)
    password = tk.Label(canvas_2, text="Password:", font=("Arial", 15),anchor="center")
    password.grid(row=4, column=1,ipady=5)
    password_entry = tk.Entry(canvas_2, font=("Arial", 10),justify='left',width=30,show="•")
    password_entry.grid(row=4, column=2)
  
    

    def find():
        user = user_name_entry.get()
        password = password_entry.get()
        def check_username_password():
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    for line in file:
                        # Strip whitespace and split by spaces or any delimiter like ',' or ':'
                        line = line.strip()
                        parts = line.split()
                        if len(parts) >= 2:  # Ensure line has both username and password
                            file_username, file_password = parts[0], parts[1]
                            if file_username == user and file_password == password:
                                return True
                return False
            except FileNotFoundError:
                print(f"Error: File '{file_path}' not found.")
                return False
            except Exception as e:
                print(f"An error occurred: {e}")
                return False

        # Example usage
        file_path = file_name
        if check_username_password():
            print(f"Username '{user}' and password '{password}' matched in the file.")
        else:
            print(f"Username '{user}' and password '{password}' did not match or were not found.")   

 
    Check = tk.Button(canvas_2, text="Check", font=("Arial", 15),anchor="center",command=find)
    Check.grid(row=5, column=2,ipadx=5)
    def back():
        canvas_2.destroy()
        

    back_1 = tk.Button(canvas_2, text="Back", font=("Arial", 15),anchor="center",command=back)
    back_1.grid(row=5, column=1)
   
def new_sign():
    canvas_3 = tk.Canvas(win, height=500, width=300)
    canvas_3.place(x=0, y=0)
    label_n = tk.Label(canvas_3, text="New user window", font=("Arial", 20),anchor="center")
    label_n.grid(row=0, column=1,columnspan=2)  
    user_name_n = tk.Label(canvas_3, text="User name:", font=("Arial", 15),anchor="center")
    user_name_n.grid (row=3, column=1,ipady=5)
    user_name_entry_n = tk.Entry(canvas_3, font=("Arial", 10),justify='left',width=30)
    user_name_entry_n.grid(row=3, column=2)
    passworda_n = tk.Label(canvas_3, text="Password:", font=("Arial", 15),anchor="center")
    passworda_n.grid(row=4, column=1,ipady=5)
    password_entry_n = tk.Entry(canvas_3, font=("Arial", 10),justify='left',width=30,show="•")
    password_entry_n.grid(row=4, column=2)
    def save_data():
        user = user_name_entry_n.get()
        password = password_entry_n.get()
        with open(file_name, "a") as file:
            file.write(user + ' ' + password + "\n")
            print(f"{user,password} saved successfully.")
    def back():
        canvas_3.destroy()
        

    creat = tk.Button(canvas_3, text="Create account", font=("Arial", 15),anchor="center",command= save_data)
    creat.grid(row=5, column=2,ipadx=5)
    back_2 = tk.Button(canvas_3, text="Back", font=("Arial", 15),anchor="center",command=back)
    back_2.grid(row=5, column=1)

# Create a canvas----------------------------------------------------------
load_data()
canvas_1 = tk.Canvas(win, height=200, width=300)
canvas_1.pack()
# Create a label
label = tk.Label(canvas_1, text="Coustumers window", font=("Arial", 20),anchor="center")
label.pack(side="top")

# Create two buttons
already_sign = tk.Button(canvas_1, text="Old user", font=("Arial", 15),anchor="center",command=already_sign)
already_sign.pack(side="left", padx=25, pady=10)

new_sign = tk.Button(canvas_1, text="New user", font=("Arial", 15),anchor="center",command=new_sign)
new_sign.pack(side="right", padx=25, pady=10)








win.mainloop()
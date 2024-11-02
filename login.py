#  Importing Libraies
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageFilter
from tkinter import messagebox

import mysql.connector as sql

'''
## SWITCH BETWEEN THE LIGHT AND DARK MODE FUNCTIONALITY

def switch_event():
    value = mode_var.get()
    if value == "off":
        ctk.set_appearance_mode("dark")
    else:
        ctk.set_appearance_mode("light")

mode_var = ctk.StringVar(value="off")
mode = ctk.CTkSwitch(master=frame, text="", command=switch_event,
                                 variable=mode_var, onvalue="on", offvalue="off")
mode.place(x=240, y = 10, anchor = 'nw')

'''

def login():
    username = user_entry.get()
    password = pass_entry.get()

    if username == '' or password == '':
        messagebox.showerror("Error!!","All fields are required")
    else:
        try:
            conn = sql.connect(host='localhost', user='root', password='12345', database = 'TkDBProject')
            #if conn.is_connected():
            #    print("connected")

            cursor = conn.cursor()

            # Query to check if the user and password exist
            query = "SELECT * FROM login WHERE user = %s AND password = %s"
            values = (username, password)

            cursor.execute(query, values)
            result = cursor.fetchone()

            if result:
                messagebox.showinfo("Success!", "Login is Successful")
                cursor.close()
                conn.close()
                root.withdraw()  # Hide the login window
                import Dasboard
            else:
                messagebox.showerror("Error!!",'Wrong Credentials')
        except:
            messagebox.showerror("Connection", "Database Connection not stablish!")


def frgt_pass():
    response = messagebox.askyesno("Confirmation", "Do you want to proceed to reset your password?")
    if response:
        root.destroy()  # Hide the login window
        import frgt_pass
    else:
        messagebox.showinfo("Cancelled", "The action was cancelled.")


# Create the main window
root = ctk.CTk()
root.geometry("600x440")
root.resizable(False,False)

'''
root.geometry('1920x1080')
root.state('zoomed')
root.resizable(0,0)
'''
root.title("Login")
root.iconbitmap(r'.\assets\window_icon.ico')

# Setting Backgroung Image
background_image = ctk.CTkImage(light_image=Image.open(r".\assets\background_img1.png").filter(ImageFilter.GaussianBlur(6)),size=(600,440))

# Create a label widget to hold the background image
bg_label=ctk.CTkLabel(master=root, image=background_image, text="")
bg_label.pack()

frame = ctk.CTkFrame(master= bg_label, width=320, height=360, fg_color="#2E2F33", corner_radius=22, bg_color="#676767")
frame.place(relx=0.5, rely=0.5, anchor = tk.CENTER)


# Setting login img
#login_img = ImageTk.PhotoImage(Image.open(r"assets\login_img1.png").resize((100,100)))
login_img = ctk.CTkImage(Image.open(r".\assets\login_img2.png"), size=(80,80))

# Create a label widget to hold the background image
login_img_label=ctk.CTkLabel(master=frame, image=login_img, text="")
login_img_label.place(x=160, y=60, anchor = tk.CENTER)

user_entry = ctk.CTkEntry(master = frame, 
                          height=38,
                          width = 220, 
                          placeholder_text="Username", 
                          placeholder_text_color="#A4A6AC", 
                          fg_color="white", 
                          text_color="black",
                          font=("Century Gothic",12, 'bold'),
                          border_width=0, 
                          corner_radius=20)
user_entry.place(x=50, y = 120)

pass_entry = ctk.CTkEntry(master = frame, 
                          height=38,
                          width = 220, 
                          placeholder_text="Password", 
                          placeholder_text_color="#A4A6AC", 
                          fg_color="white", 
                          text_color="black",
                          font=("Century Gothic",12, 'bold'),
                          border_width=0, 
                          corner_radius=20,
                          show = '*')
pass_entry.place(x=50, y = 175)

login_button = ctk.CTkButton(master=frame, 
                             width=220, 
                             corner_radius=18, 
                             text="Login", 
                             border_spacing=10,
                             font=("Century Gothic",15, 'bold'),
                             command=login)

login_button.place(x=50, y=248)

'''
frgt_pass_label = ctk.CTkLabel(master=frame, text="Forget Password?", font=('Century Gothic', 12), cursor="hand2")
frgt_pass_label.place(x=160, y=305, anchor = tk.CENTER)

frgt_pass_label.bind("<Button-1>", frgt_pass)
'''

frgt_button = ctk.CTkButton(master=frame,
                            text="Forget Password?", 
                            font=('Century Gothic', 12), 
                            fg_color="#2E2F33",
                            hover=None,
                            command=frgt_pass)

frgt_button.place(x=163, y=305, anchor = tk.CENTER)


root.mainloop()
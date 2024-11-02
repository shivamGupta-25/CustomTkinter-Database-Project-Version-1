#  Importing Libraies

import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageFilter
from tkinter import messagebox
import mysql.connector as sql

#username = None
def Continue():
    #global username
    user_id = user_entry.get()
    #username = user_id
    if user_id =='':
        messagebox.showerror("Error!","Please Enter Username")
    else:
        try:
            conn = sql.connect(host='localhost', user='root', password='12345', database = 'TkDBProject')
            #if conn.is_connected():
            #    print("connected")

            cursor = conn.cursor()

            # Query to check if the user exist
            query = "SELECT * FROM login WHERE user like %s"
            values = (user_id,)
            cursor.execute(query, values)
            record = cursor.fetchone()
            if record and record[0] == user_id:
                cursor.close()
                conn.close()
                root.destroy()
                import reset_pass
                reset_pass.reset_password(user_id)
            else:
                messagebox.showerror("Invalid User","User not found or incorrect Username")
        except:
            messagebox.showerror("Connection", "Database Connection not stablish!")
            
# Create the main window
root = ctk.CTk()
root.geometry("600x440")
root.resizable(False,False)

root.title("Forget Password")
root.iconbitmap(r'.\assets\frgt_window_icon.ico')

# Setting Backgroung Image
background_image = ctk.CTkImage(Image.open(r".\assets\background_img1.png").filter(ImageFilter.GaussianBlur(6)),size=(600,440))

# Create a label widget to hold the background image
bg_label=ctk.CTkLabel(master=root, image=background_image, text="")
bg_label.pack()


# FRAME

frame = ctk.CTkFrame(master= bg_label, width=320, height=320, fg_color="#2E2F33", corner_radius=22, bg_color="#676767")
frame.place(relx=0.5, rely=0.5, anchor = tk.CENTER)

# Setting forget pass img

frgt_pass_img = ctk.CTkImage(Image.open(r".\assets\frgt_pass_img.png"), size = (80, 80))

# Create a label widget to hold the forget pass image
frgtPass_img_label=ctk.CTkLabel(master=frame, image=frgt_pass_img, text="")
frgtPass_img_label.place(x=160, y=60, anchor = tk.CENTER)

# Labels

l1= ctk.CTkLabel(master= frame, text = "Find your account", font=("Calibri Light", 25, 'bold'))
l1.place(x=15, y=98)

l2= ctk.CTkLabel(master= frame, text = "Enter your username", font=("Candara", 12))
l2.place(x=15, y=126)



user_entry = ctk.CTkEntry(master = frame, 
                          height=38,
                          width = 220, 
                          placeholder_text="Username", 
                          placeholder_text_color="#A4A6AC", 
                          fg_color="white", 
                          text_color="black",
                          font=("Century Gothic",12, 'bold'),
                          border_width=0, 
                          corner_radius=8)
user_entry.place(x=50, y = 170)

continue_button = ctk.CTkButton(master=frame, 
                             width=220, 
                             corner_radius=50, 
                             text="Continue", 
                             border_spacing=10,
                             font=("Century Gothic",15, 'bold'),
                             command= Continue)

continue_button.place(x=50, y=233)



root.mainloop()
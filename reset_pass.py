#  Importing Libraies

import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageFilter
from tkinter import messagebox
import mysql.connector as sql

def reset_password(user_id):
    def ResetPassword():
        passwrd = newPass_entry1.get()
        passwrd_repeat = newPass_entry2.get()

        if passwrd == '' or passwrd_repeat == '':
            messagebox.showerror("Error!", "Field is required")
        elif passwrd == passwrd_repeat:
            try:
                conn = sql.connect(host='localhost', user='root', password='12345', database = 'TkDBProject')
                #if conn.is_connected():
                #    print("connected")

                cursor = conn.cursor()

                # Query to check if the user exist
                query = "update login set password = %s where user = %s"
                values=(passwrd, user_id)
                cursor.execute(query, values)
                conn.commit()

                query = "SELECT * FROM login WHERE user = %s AND password = %s"
                values = (user_id, passwrd)

                cursor.execute(query, values)
                result = cursor.fetchone()
                user = result[0]
                pswrd = result[1]

                if user == user_id and pswrd == passwrd:
                    messagebox.showinfo(message="Password Successfully reset")
                    cursor.close()
                    conn.close()
                    root.destroy()
                    import login
            except:
                messagebox.showerror("Connection", "Database Connection not stablish!")
        else:
            messagebox.showerror(message="Entered password is not same")


    def cancel():
        message = messagebox.askquestion(message="Do you want to cancel?")
        if message == "yes":
            root.destroy()
            import login

    # Create the main window
    root = ctk.CTk()
    root.geometry("600x550")
    root.resizable(False,False)

    root.title("Reset Password")
    root.iconbitmap(r'.\assets\reset_pass_window_icon.ico')

    # Setting Backgroung Image
    background_image = ctk.CTkImage(Image.open(r".\assets\background_img1.png").filter(ImageFilter.GaussianBlur(6)),size=(600,550))

    # Create a label widget to hold the background image
    bg_label=ctk.CTkLabel(master=root, image=background_image, text="")
    bg_label.pack()


    # FRAME

    frame = ctk.CTkFrame(master= bg_label, width=320, height=450, fg_color="#2E2F33", corner_radius=22, bg_color="#676767")
    frame.place(relx=0.5, rely=0.5, anchor = tk.CENTER)

    # Setting forget pass img

    new_pass_img = ctk.CTkImage(Image.open(r".\assets\reset_password.png"), size= (80,80))

    # Create a label widget to hold the forget pass image
    newPass_img_label=ctk.CTkLabel(master=frame, image=new_pass_img, text="")
    newPass_img_label.place(x=160, y=55, anchor = tk.CENTER)

    # Labels

    l1= ctk.CTkLabel(master= frame, text = "Create A Strong Password", font=("Calibri Light", 22, 'bold'))
    l1.place(x=160, y=110, anchor = tk.CENTER)

    l2= ctk.CTkLabel(master= frame, text = "Your Password must be at least 6 character", font=("Candara", 12))
    l3= ctk.CTkLabel(master= frame, text = "and should include a combination of numbers,", font=("Candara", 12))
    l4= ctk.CTkLabel(master= frame, text = "letters and special character(!$@%)", font=("Candara", 12))

    l2.place(x=160, y=135, anchor = tk.CENTER)
    l3.place(x=160, y=154, anchor = tk.CENTER)
    l4.place(x=160, y=174, anchor = tk.CENTER)



    newPass_entry1 = ctk.CTkEntry(master = frame, 
                            height=38,
                            width = 220, 
                            placeholder_text="New Password", 
                            placeholder_text_color="#A4A6AC", 
                            fg_color="white", 
                            text_color="black",
                            font=("Century Gothic",12, 'bold'),
                            border_width=0, 
                            corner_radius=8,
                            show="*")
    newPass_entry1.place(x=50, y = 195)

    newPass_entry2 = ctk.CTkEntry(master = frame, 
                            height=38,
                            width = 220, 
                            placeholder_text="New Password, again", 
                            placeholder_text_color="#A4A6AC", 
                            fg_color="white", 
                            text_color="black",
                            font=("Century Gothic",12, 'bold'),
                            border_width=0, 
                            corner_radius=8,
                            show="*")
    newPass_entry2.place(x=50, y = 250)

    reset_button = ctk.CTkButton(master=frame, 
                                width=220, 
                                corner_radius=50, 
                                text="Reset Password", 
                                border_spacing=10,
                                font=("Century Gothic",15, 'bold'),
                                command= ResetPassword)

    reset_button.place(x=50, y=320)

    cancel_button = ctk.CTkButton(master=frame, 
                                width=220, 
                                corner_radius=50, 
                                text="Cancel", 
                                border_spacing=10,
                                font=("Century Gothic",15, 'bold'),
                                command= cancel)

    cancel_button.place(x=50, y=375)




    root.mainloop()
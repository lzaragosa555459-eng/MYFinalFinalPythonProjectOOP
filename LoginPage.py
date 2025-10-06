import tkinter as tk
from PIL import Image, ImageTk
import subprocess


root = tk.Tk()
root.title("Login")
root.configure(bg="#1E1E3F")
root.resizable(False,False)
root.geometry("450x620")

panel1 =  tk.Frame(root, bg = "#1E1E3F", width = 200, height = 330) 
panel1.pack(side="left",fill="y")
panel2 = tk.Frame(root, bg = "#2D2B55", width = 260, height = 330) 
panel2.pack(side="right",fill="y")

img = Image.open(r"C:\Users\User\Downloads\car.png")
img = img.resize((100,100))
tk_img = ImageTk.PhotoImage(img)
label = tk.Label(panel1, image=tk_img, bg="#1E1E3F")
label.image = tk_img
label.place(relx=0.5, rely = 0.4, anchor = tk.CENTER)

labelTitle = tk.Label(panel1, text="WELCOME!",bg = "#1E1E3F", font=("Candara",12), fg='#A599E9').place(relx=0.5, rely = 0.1, anchor = tk.CENTER)
labelTitle1 = tk.Label(panel1, text="CAR RENTALS AND",bg = "#1E1E3F", font=("Verdana",10), fg='#FAD000').place(relx=0.5, rely = 0.5, anchor = tk.CENTER)
labelTitle1 = tk.Label(panel1, text="SERVICES",bg = "#1E1E3F", font=("Verdana",10), fg='#FAD000').place(relx=0.5, rely = 0.54, anchor = tk.CENTER)

labelTitle = tk.Label(panel2, text="LOGIN CUSTOMER",bg = "#2D2B55", font=("Arial",14,'bold'), fg='#A599E9').place(relx=0.5, rely = 0.1, anchor = tk.CENTER)

panel2InnerFrame = tk.Frame(panel2,  bg = "#2D2B55", width = 200, height = 200)
panel2InnerFrame.place(relx=0.5, rely = 0.5, anchor = tk.CENTER)


labelName = tk.Label(panel2InnerFrame, fg="#A599E9", bg = "#2D2B55", text="Name")
labelName.grid(row=0, column=0, padx=0, pady=10, sticky="e")

EnterName = tk.Entry(panel2InnerFrame, width=30, highlightthickness=2,highlightcolor="#1E1E3F", highlightbackground="#2D2B55")
EnterName.grid(row=0, column=1, padx=0, pady=10) 

labelPassword = tk.Label(panel2InnerFrame,fg="#A599E9" ,bg = "#2D2B55", text="Password") 
labelPassword.grid(row=1, column=0, padx=0, pady=0, sticky="e")

EnterPassword = tk.Entry(panel2InnerFrame, show = "*", width=30, highlightthickness=2, highlightcolor="#1E1E3F", highlightbackground="#2D2B55")
EnterPassword.grid(row=1, column=1, padx=0, pady=10)

def login():
    username = EnterName.get()
    password = EnterPassword.get()
    if username == "Admin" and password == "1234":
        root.destroy()
        subprocess.Popen(["python","MainFrame.py"])

    elif username == "Liz Zaragosa" and password == "217":
        root.destroy()
        subprocess.Popen(["python","CustomerForm.py"])
    else:
        label = tk.Label(panel2InnerFrame, text="Invalid Credentials. try again!", bg = "#2D2B55",fg="#A599E9")
        label.grid(row=3, column=1, padx=10, pady=10)


LoginButton = tk.Button(panel2InnerFrame, text="Login", command=login, borderwidth = 2, highlightthickness=0,bg="#1E1E3F",fg="#A599E9",highlightcolor="goldenrod",highlightbackground="black")
LoginButton.grid(row=2, column=1, padx=10, pady=10)



root.mainloop()
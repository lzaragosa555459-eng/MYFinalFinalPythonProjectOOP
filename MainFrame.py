import tkinter as tk
from tkinter import ttk
from Customer import CustomerFrame
from Payment import PaymentFrame
from Rentals import RentalFrame
from Vehicle import VehicleFrame
from Reports import ReportFrame
from PIL import Image, ImageTk


class mainFrame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Admin Car Rentals and Services")
        self.geometry("650x500")
        self.resizable(False,False)
        self.configure(bg="lightgrey")
    
        #2D2B55 - normal purple
        #1E1E3F -  dark purple
        #FAD000 - golden
        #A599E9 - foreground
        self.LeftMainMenuFrame = tk.Frame(self, bg = "#1E1E3F", width = 200, height = 500)
        self.LeftMainMenuFrame.pack(side="left",fill="y")
        self.RightFrame = tk.Frame(self, bg="#2D2B55",width = 500, height = 330)
        self.RightFrame.pack(side="right",fill="y")

        style = ttk.Style()
        style.theme_use("default")
        LeftMainMenuFrameUpperLogo = tk.Frame(self.LeftMainMenuFrame,height=140, width = 120, bg="#1E1E3F")
        LeftMainMenuFrameUpperLogo.pack(padx=10,pady=5)

        

        img = Image.open(r"C:\Users\User\Downloads\car.png")
        img = img.resize((80,80))
        tk_img = ImageTk.PhotoImage(img)
        label = tk.Label(LeftMainMenuFrameUpperLogo, image=tk_img, bg="#1E1E3F")
        label.image = tk_img
        label.place(relx=0.5, rely = 0.42, anchor = tk.CENTER)

        label = tk.Label(self.LeftMainMenuFrame,text="ADMIN",font=("Arial",10,"bold"),bg="#1E1E3F",fg="#A599E9").place(relx=0.5, rely = 0.233, anchor = tk.CENTER)

        button_to_Customers = tk.Button(self.LeftMainMenuFrame, text="Customers", width = 21, command=lambda:self.show_frame("CustomerFrame"),relief = 'flat', borderwidth = 2,bd=0,bg="#1E1E3F",fg="#A599E9",activebackground="#1E1E3F",activeforeground="#A599E9")
        button_to_Customers.pack(pady=5)
        button_to_Payment = tk.Button(self.LeftMainMenuFrame, text="Payment", width = 15,command=lambda:self.show_frame("PaymentFrame"),relief = 'flat', borderwidth = 2,bd=0,bg="#1E1E3F",fg="#A599E9",highlightbackground="#1E1E3F",activebackground="#1E1E3F",activeforeground="#A599E9")
        button_to_Payment.pack(pady=5)
        button_to_Rentals = tk.Button(self.LeftMainMenuFrame, text="Rentals", width = 15,command=lambda:self.show_frame("RentalFrame"),relief = 'flat', borderwidth = 2,bd=0,bg="#1E1E3F",fg="#A599E9",highlightbackground="#1E1E3F",activebackground="#1E1E3F",activeforeground="#A599E9")
        button_to_Rentals.pack(pady=5)
        button_to_Vehicle = tk.Button(self.LeftMainMenuFrame, text="Vehicle", width = 15,command=lambda:self.show_frame("VehicleFrame"),relief = 'flat', borderwidth = 2,bd=0,bg="#1E1E3F",fg="#A599E9",highlightbackground="#1E1E3F",activebackground="#1E1E3F",activeforeground="#A599E9")
        button_to_Vehicle.pack(pady=5)
        button_to_Reports = tk.Button(self.LeftMainMenuFrame, text="History", width = 15,command=lambda:self.show_frame("ReportFrame"),relief = 'flat', borderwidth = 2,bd=0,bg="#1E1E3F",fg="#A599E9",highlightbackground="#1E1E3F",activebackground="#1E1E3F",activeforeground="#A599E9")
        button_to_Reports.pack(pady=5)
        button_to_Exit = tk.Button(self.LeftMainMenuFrame, text="Exit", width = 10, command=self.destroy,relief = 'flat', borderwidth = 2,bg="#1E1E3F",bd=0,fg="#A599E9",activebackground="#1E1E3F",activeforeground="#A599E9")
        button_to_Exit.pack(pady=50)

        

        self.frames={}

        for F in (CustomerFrame,PaymentFrame,RentalFrame,VehicleFrame,ReportFrame):
            page_name = F.__name__
            frame = F(self.RightFrame,self)
            frame.configure(bg="#2D2B55")
            self.frames[page_name] = frame
            frame.place(x=0, y=0, width=550, height=500)


        self.show_frame("CustomerFrame")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        

if __name__=="__main__":
    app = mainFrame()
    app.mainloop()
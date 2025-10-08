import tkinter as tk
from tkinter import ttk
from sql import loadPayment, add_to_table1,Update1,Delete1
class PaymentFrame(tk.Frame):
    def __init__(self, parent,controller):
        super().__init__(parent)
        self.PaymentLabel = tk.Label(self, text="Payment Record", bg="#2D2B55",fg="#FAD000")
        self.PaymentLabel.pack()

        self.InnerFramePayment1 = tk.Frame(self,  bg = "#2D2B55", width = 550, height = 200) 
        self.InnerFramePayment1.pack(side="top",fill="y",anchor="center",pady=15)

        paymentid_var = tk.StringVar()
        paymentMethod_var = tk.StringVar()
        Date_var = tk.StringVar()
        amount_var = tk.StringVar()
        rental_var  = tk.StringVar()

        InnerFramePayment1Ver2 = tk.Frame(self.InnerFramePayment1,bg="#2D2B55", height = 50)
        InnerFramePayment1Ver2.place(relx=0.28, rely = 0.5, anchor ="center")

        InnerFramePayment1Ver3 = tk.Frame(self.InnerFramePayment1,bg="#2D2B55", height = 50)
        InnerFramePayment1Ver3.place(relx=0.6, rely = 0.5, anchor ="center")

        labelPaymentID = tk.Label(InnerFramePayment1Ver2,bg="#2D2B55", text="PaymentID",fg="white")
        labelPaymentID.grid(row=0, column=0, padx=0, pady=10, sticky="e")

        Enter_PaymentID = tk.Entry(InnerFramePayment1Ver2, width=20, textvariable=paymentid_var,relief="flat",bg="white")
        Enter_PaymentID.grid(row=0, column=1, padx=0, pady=10) 

        LayoutPaymentMethod = tk.Label(InnerFramePayment1Ver2,bg="#2D2B55", text="Payment Method",fg="white") 
        LayoutPaymentMethod.grid(row=1, column=0, padx=0, pady=10, sticky="e")
        
        Enter_PaymentMethod = tk.Entry(InnerFramePayment1Ver2, width=20, textvariable=paymentMethod_var,relief="flat",bg="white")
        Enter_PaymentMethod.grid(row=1, column=1, padx=0, pady=10)

        PaymentDate = tk.Label(InnerFramePayment1Ver2,bg="#2D2B55", text="Date",fg="white") 
        PaymentDate.grid(row=2, column=0, padx=0, pady=10, sticky="e")
        
        Enter_PaymentDate = tk.Entry(InnerFramePayment1Ver2, width=20, textvariable=Date_var,relief="flat",bg="white")
        Enter_PaymentDate.grid(row=2, column=1, padx=0, pady=10)

        labelAmount = tk.Label(InnerFramePayment1Ver2,bg="#2D2B55", text="Amount",fg="white") 
        labelAmount.grid(row=3, column=0, padx=0, pady=10, sticky="e")
        
        Enter_Amount = tk.Entry(InnerFramePayment1Ver2, width=20, textvariable=amount_var,relief="flat",bg="white")
        Enter_Amount.grid(row=3, column=1, padx=0, pady=10)

        labelRentalID = tk.Label(InnerFramePayment1Ver2,bg="#2D2B55", text="RentalID",fg="white") 
        labelRentalID.grid(row=4, column=0, padx=0, pady=10, sticky="e")
        
        Enter_Rental = tk.Entry(InnerFramePayment1Ver2, width=20, textvariable=rental_var,relief="flat",bg="white")
        Enter_Rental.grid(row=4, column=1, padx=0, pady=10)

        

        self.InnerFramePayment2 = tk.Frame(self,  bg = "#2D2B55", width = 550, height = 550) 
        self.InnerFramePayment2.pack(side="bottom",fill="y")

        tablePayment = ttk.Treeview(self.InnerFramePayment2,columns=("PaymentID","PaymentMethod","Date","Amount","RentalID"), show="headings",height=10)
        tablePayment.heading("PaymentID",text="PaymentID")
        tablePayment.heading("PaymentMethod", text="PaymentMethod")
        tablePayment.heading("Date", text="Date")
        tablePayment.heading("Amount", text="Amount")
        tablePayment.heading("RentalID", text="RentalID")

        tablePayment.column("PaymentID",width=70, anchor="w")
        tablePayment.column("PaymentMethod", width=130, anchor="w")
        tablePayment.column("Date", width=100, anchor="w")
        tablePayment.column("Amount", width=105, anchor="w")
        tablePayment.column("RentalID", width=70, anchor="w")
        tablePayment.place(relx =0.45,rely =0.5, anchor="center")
    
        def DeleteEntry():
            Enter_PaymentID.delete(0, tk.END)
            Enter_PaymentMethod.delete(0, tk.END)
            Enter_PaymentDate.delete(0, tk.END)
            Enter_Amount.delete(0, tk.END)
            Enter_Rental.delete(0, tk.END)
            
            
        def on_select(event):
            global selected_id
            focus = tablePayment.focus()
            if not focus: return
            vals = tablePayment.item(focus)["values"]
            if vals:
                selected_id = vals[0]
                paymentid_var.set(vals[0])
                paymentMethod_var.set(vals[1])
                Date_var.set(vals[2])
                amount_var.set(vals[3])
                rental_var.set(vals[4])
            else:
                selected_id = None
        tablePayment.bind("<<TreeviewSelect>>", on_select)
        
        def add():
            id = Enter_PaymentID.get()
            method = Enter_PaymentMethod.get()
            payment = Enter_PaymentDate.get()
            amount = Enter_Amount.get()
            rental = Enter_Rental.get()
            add_to_table1(tablePayment,id,method,payment,amount,rental)
            DeleteEntry()
        def update():
            Update1(tablePayment,paymentid_var,paymentMethod_var,Date_var,amount_var,rental_var,selected_id)
            DeleteEntry()
        def delete():
            Delete1(tablePayment)
            DeleteEntry()
        loadPayment(tablePayment)

        AddButton = tk.Button(InnerFramePayment1Ver3, text="Add",width=10, command=add,bg="#A599E9")
        AddButton.grid(row=2, column=1, padx=10, pady=10)

        UpdateButton = tk.Button(InnerFramePayment1Ver3,text="Update", width=10,command=update,bg="#A599E9")
        UpdateButton.grid(row=3, column=1, padx=10, pady=10)

        DeleteButton = tk.Button(InnerFramePayment1Ver3,text="Delete", width=10,command=delete,bg="#A599E9")
        DeleteButton.grid(row=4, column=1, padx=10, pady=10)
import tkinter as tk
from tkinter import ttk
from sql import loadRentals, add_to_table2 ,Update2,Delete2

class RentalFrame(tk.Frame):
    def __init__(self, parent,controller):
        super().__init__(parent)
        self.PaymentLabel = tk.Label(self, text="Rental Record", bg="#2D2B55",fg="#FAD000")
        self.PaymentLabel.pack()

        self.InnerFramePayment1 = tk.Frame(self,  bg = "#2D2B55", width = 550, height = 200) 
        self.InnerFramePayment1.pack(side="top",fill="y",anchor="center",pady=15)
        
        rentalid_var = tk.StringVar()
        rentaldate_var = tk.StringVar()
        returndate_var = tk.StringVar()
        customerid_var  = tk.StringVar()
        vehicleid_var  = tk.StringVar()

        InnerFrameRental1Ver2 = tk.Frame(self.InnerFramePayment1,bg="#2D2B55", height = 80)
        InnerFrameRental1Ver2.place(relx=0.35, rely = 0.5, anchor ="center")

        InnerFrameRental1Ver3 = tk.Frame(self.InnerFramePayment1,bg="#2D2B55", height = 50)
        InnerFrameRental1Ver3.place(relx=0.80, rely = 0.5, anchor ="center")

        labelCustomerID = tk.Label(InnerFrameRental1Ver2,bg="#2D2B55", text="PaymentID",fg="#A599E9")
        labelCustomerID.grid(row=0, column=0, padx=0, pady=10, sticky="e")

        Enter_RentalID = tk.Entry(InnerFrameRental1Ver2, width=15, textvariable=rentalid_var,relief="flat",bg="#A599E9")
        Enter_RentalID.grid(row=0, column=1, padx=(0,68), pady=10) 

        LayoutRentalDate = tk.Label(InnerFrameRental1Ver2,bg="#2D2B55", text="Payment Method",fg="#A599E9")
        LayoutRentalDate.grid(row=1, column=0, padx=0, pady=10, sticky="e")
        
        Enter_RentalDate = tk.Entry(InnerFrameRental1Ver2, width=15, textvariable=rentaldate_var,relief="flat",bg="#A599E9")
        Enter_RentalDate.grid(row=1, column=1, padx=(0,68), pady=10)

        ReturnDate = tk.Label(InnerFrameRental1Ver2,bg="#2D2B55", text="Date",fg="#A599E9") 
        ReturnDate.grid(row=2, column=0, padx=0, pady=10, sticky="e")
        
        Enter_ReturnDate = tk.Entry(InnerFrameRental1Ver2, width=15, textvariable=returndate_var,relief="flat",bg="#A599E9")
        Enter_ReturnDate.grid(row=2, column=1, padx=(0,68), pady=10)

        labelCustomerID = tk.Label(InnerFrameRental1Ver2,bg="#2D2B55", text="CustomerID",fg="#A599E9") 
        labelCustomerID.grid(row=0, column=1, padx=(50,0), pady=10, sticky="e")
        
        Enter_CustomerID = tk.Entry(InnerFrameRental1Ver2, width=13, textvariable=customerid_var,relief="flat",bg="#A599E9")
        Enter_CustomerID.grid(row=0, column=2, padx=0, pady=10)

        labelVehicleID = tk.Label(InnerFrameRental1Ver2,bg="#2D2B55", text="VehicleID",fg="#A599E9") 
        labelVehicleID.grid(row=1, column=1, padx=0, pady=10, sticky="e")
        
        Enter_VehicleID = tk.Entry(InnerFrameRental1Ver2, width=13, textvariable=vehicleid_var,relief="flat",bg="#A599E9")
        Enter_VehicleID.grid(row=1, column=2, padx=0, pady=10)
        

        self.InnerFramePayment2 = tk.Frame(self,  bg = "#2D2B55", width = 550, height = 550) 
        self.InnerFramePayment2.pack(side="bottom",fill="y")

        tableRentals = ttk.Treeview(self.InnerFramePayment2,columns=("RentalID","RentalDate","ReturnDate","CustomerID","VehicleID"), show="headings",height=10)
        tableRentals.heading("RentalID",text="RentalID")
        tableRentals.heading("RentalDate", text="RentalDate")
        tableRentals.heading("ReturnDate", text="ReturnDate")
        tableRentals.heading("CustomerID", text="CustomerID")
        tableRentals.heading("VehicleID", text="VehicleID")

        tableRentals.column("RentalID",width=70, anchor="w")
        tableRentals.column("RentalDate", width=130, anchor="w")
        tableRentals.column("ReturnDate", width=130, anchor="w")
        tableRentals.column("CustomerID", width=75, anchor="w")
        tableRentals.column("VehicleID", width=70, anchor="w")
        tableRentals.place(relx =0.45,rely =0.5, anchor="center")
    
        def DeleteEntry():
            Enter_RentalID.delete(0, tk.END)
            Enter_RentalDate.delete(0, tk.END)
            Enter_ReturnDate.delete(0, tk.END)
            Enter_CustomerID.delete(0, tk.END)
            Enter_VehicleID.delete(0, tk.END)
            
            
        def on_select(event):
            global selected_id
            focus = tableRentals.focus()
            if not focus: return
            vals = tableRentals.item(focus)["values"]
            if vals:
                selected_id = vals[0]
                rentalid_var.set(vals[0])
                rentaldate_var.set(vals[1])
                returndate_var.set(vals[2])
                customerid_var.set(vals[3])
                vehicleid_var.set(vals[4])
            else:
                selected_id = None
        tableRentals.bind("<<TreeviewSelect>>", on_select)
        
        def add():
            id = Enter_RentalID.get()
            rentalDate = Enter_RentalDate.get()
            returnDate = Enter_ReturnDate.get()
            customerid = Enter_CustomerID.get()
            vehicleid = Enter_VehicleID.get()
            add_to_table2(tableRentals,id,rentalDate,returnDate,customerid,vehicleid)
            DeleteEntry()
        def update():
            Update2(tableRentals,rentalid_var,rentaldate_var,returndate_var,customerid_var,vehicleid_var,selected_id)
            DeleteEntry()
        def delete():
            Delete2(tableRentals)
            DeleteEntry()
        loadRentals(tableRentals)

        AddButton = tk.Button(InnerFrameRental1Ver3, text="Add",width=10, command=add,bg="#A599E9")
        AddButton.grid(row=2, column=1, padx=10, pady=10)

        UpdateButton = tk.Button(InnerFrameRental1Ver3,text="Update", width=10,command=update,bg="#A599E9")
        UpdateButton.grid(row=3, column=1, padx=10, pady=10)

        DeleteButton = tk.Button(InnerFrameRental1Ver3,text="Delete", width=10,command=delete,bg="#A599E9")
        DeleteButton.grid(row=4, column=1, padx=10, pady=10)
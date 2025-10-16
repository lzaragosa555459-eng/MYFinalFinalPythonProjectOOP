import tkinter as tk
from tkinter import ttk
from sql import loadVehicle, Delete3, Update3
    
class VehicleFrame(tk.Frame):
    def __init__(self, parent,controller):
        super().__init__(parent)
        self.PaymentLabel = tk.Label(self, text="Vehicle Record", bg="#2D2B55",fg="#FAD000")
        self.PaymentLabel.pack()

        self.InnerFramePayment1 = tk.Frame(self,  bg = "#2D2B55", width = 550, height = 200) 
        self.InnerFramePayment1.pack(side="top",fill="y",anchor="center",pady=15)

        vehicleid_var = tk.StringVar()
        type_var = tk.StringVar()
        make_var = tk.StringVar()
        model_var = tk.StringVar()
        totalcost_var = tk.StringVar()


        InnerFrameVehicle1Ver2 = tk.Frame(self.InnerFramePayment1,bg="#2D2B55", height = 50)
        InnerFrameVehicle1Ver2.place(relx=0.3, rely = 0.5, anchor ="center")

        InnerFrameVehicle1Ver3 = tk.Frame(self.InnerFramePayment1,bg="#2D2B55", height = 50)
        InnerFrameVehicle1Ver3.place(relx=0.6, rely = 0.5, anchor ="center")

        labelID = tk.Label(InnerFrameVehicle1Ver2,bg="#2D2B55", text="Customer ID",fg="white")
        labelID.grid(row=0, column=0, padx=0, pady=10, sticky="w")

        Enter_ID = tk.Entry(InnerFrameVehicle1Ver2, width=20, textvariable=vehicleid_var,relief="flat",bg="white")
        Enter_ID.grid(row=0, column=1, padx=0, pady=10) 

        labelType = tk.Label(InnerFrameVehicle1Ver2,bg="#2D2B55", text="Name",fg="white") 
        labelType.grid(row=1, column=0, padx=0, pady=10, sticky="w")
        
        Enter_Type = tk.Entry(InnerFrameVehicle1Ver2, width=20, textvariable=type_var,relief="flat",bg="white")
        Enter_Type.grid(row=1, column=1, padx=0, pady=10)

        labelMake = tk.Label(InnerFrameVehicle1Ver2,bg="#2D2B55", text="Email",fg="white") 
        labelMake.grid(row=2, column=0, padx=0, pady=10, sticky="w")
        
        Enter_Make = tk.Entry(InnerFrameVehicle1Ver2, width=20, textvariable=make_var,relief="flat",bg="white")
        Enter_Make.grid(row=2, column=1, padx=0, pady=10)

        labelModel = tk.Label(InnerFrameVehicle1Ver2,bg="#2D2B55", text="Phone",fg="white")
        labelModel.grid(row=3, column=0, padx=0, pady=10, sticky="w")
        
        Enter_Model = tk.Entry(InnerFrameVehicle1Ver2, width=20, textvariable=model_var,relief="flat",bg="white")
        Enter_Model.grid(row=3, column=1, padx=0, pady=10)

        labeltotalcost = tk.Label(InnerFrameVehicle1Ver2,bg="#2D2B55", text="Amount",fg="white") 
        labeltotalcost.grid(row=4, column=0, padx=0, pady=10, sticky="w")
        
        Enter_totalcost = tk.Entry(InnerFrameVehicle1Ver2, width=20, textvariable=totalcost_var,relief="flat",bg="white")
        Enter_totalcost.grid(row=4, column=1, padx=0, pady=10)
        self.InnerFrameVehicle2 = tk.Frame(self,  bg = "#2D2B55", width = 550, height = 550) 
        self.InnerFrameVehicle2.pack(side="bottom",fill="y")



        tableVehicle = ttk.Treeview(self.InnerFrameVehicle2,columns=("VehicleID","Type","Make","Model","TotalCost"), show="headings",height=10)
        tableVehicle.heading("VehicleID",text="VehicleID")
        tableVehicle.heading("Type", text="Type")
        tableVehicle.heading("Make", text="Make")
        tableVehicle.heading("Model", text="Model")
        tableVehicle.heading("TotalCost", text="TotalCost")
        tableVehicle.column("VehicleID",width=75, anchor="w")
        tableVehicle.column("Type", width=90, anchor="w")
        tableVehicle.column("Make", width=90, anchor="w")
        tableVehicle.column("Model", width=150, anchor="w")
        tableVehicle.column("TotalCost", width=70, anchor="w")
        tableVehicle.place(relx =0.45,rely =0.5, anchor="center")

    

        #-------------------------Function Area--------------------------
        def DeleteEntry():
            Enter_ID.delete(0, tk.END)
            Enter_Type.delete(0, tk.END)
            Enter_Make.delete(0, tk.END)
            Enter_Model.delete(0, tk.END)
            Enter_totalcost.delete(0, tk.END)
            

        def on_select(event):
            global selected_id
            focus = tableVehicle.focus()
            if not focus: return
            vals = tableVehicle.item(focus)["values"]
            if vals:
                selected_id = vals[0]
                vehicleid_var.set(vals[0])
                type_var.set(vals[1])
                make_var.set(vals[2])
                model_var.set(vals[3])
                totalcost_var.set(vals[4])
            else:
                selected_id = None
        tableVehicle.bind("<<TreeviewSelect>>", on_select)
        
        def update():
            Update3(tableVehicle,type_var,make_var,model_var,vehicleid_var,totalcost_var,selected_id)
            DeleteEntry()
        def delete():
            Delete3(tableVehicle)
            DeleteEntry()


        UpdateButton = tk.Button(InnerFrameVehicle1Ver3,text="Update", width=10, command=update,bg="#A599E9")
        UpdateButton.grid(row=3, column=1, padx=10, pady=10)

        DeleteButton = tk.Button(InnerFrameVehicle1Ver3,text="Delete", width=10, command=delete,bg="#A599E9")
        DeleteButton.grid(row=4, column=1, padx=10, pady=10)

        loadVehicle(tableVehicle)
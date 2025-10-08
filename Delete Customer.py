import tkinter as tk
from tkinter import ttk
from sql import add_to_table, Update, load, Delete

class CustomerFrame(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        
        self.CustomerLabel = tk.Label(self, text="Customer Record", bg="#2D2B55",fg="#FAD000")
        self.CustomerLabel.pack()

        self.InnerFrameCustomer1 = tk.Frame(self,  bg = "#2D2B55", width = 550, height = 200) 
        self.InnerFrameCustomer1.pack(side="top",fill="y",anchor="center",pady=15)


        id_var = tk.StringVar()
        name_var = tk.StringVar()
        email_var = tk.StringVar()
        phone_var = tk.StringVar()


        InnerFrameCustomer1Ver2 = tk.Frame(self.InnerFrameCustomer1,bg="#2D2B55", height = 50)
        InnerFrameCustomer1Ver2.place(relx=0.3, rely = 0.5, anchor ="center")

        InnerFrameCustomer1Ver3 = tk.Frame(self.InnerFrameCustomer1,bg="#2D2B55", height = 50)
        InnerFrameCustomer1Ver3.place(relx=0.6, rely = 0.5, anchor ="center")

        labelID = tk.Label(InnerFrameCustomer1Ver2,bg="#2D2B55", text="Customer ID",fg="#A599E9")
        labelID.grid(row=0, column=0, padx=0, pady=10, sticky="e")

        Enter_ID = tk.Entry(InnerFrameCustomer1Ver2, width=20, textvariable=id_var,relief="flat",bg="#A599E9")
        Enter_ID.grid(row=0, column=1, padx=0, pady=10) 

        labelName = tk.Label(InnerFrameCustomer1Ver2,bg="#2D2B55", text="Name",fg="#A599E9") 
        labelName.grid(row=1, column=0, padx=0, pady=10, sticky="e")

        Enter_Name = tk.Entry(InnerFrameCustomer1Ver2, width=20, textvariable=name_var,relief="flat",bg="#A599E9")
        Enter_Name.grid(row=1, column=1, padx=0, pady=10)

        labelEmail = tk.Label(InnerFrameCustomer1Ver2,bg="#2D2B55", text="Email",fg="#A599E9") 
        labelEmail.grid(row=2, column=0, padx=0, pady=10, sticky="e")

        Enter_Email = tk.Entry(InnerFrameCustomer1Ver2, width=20, textvariable=email_var,relief="flat",bg="#A599E9")
        Enter_Email.grid(row=2, column=1, padx=0, pady=10)

        labelPhone = tk.Label(InnerFrameCustomer1Ver2,bg="#2D2B55", text="Phone",fg="#A599E9") 
        labelPhone.grid(row=3, column=0, padx=0, pady=10, sticky="e")

        Enter_Phone = tk.Entry(InnerFrameCustomer1Ver2, width=20, textvariable=phone_var,relief="flat",bg="#A599E9")
        Enter_Phone.grid(row=3, column=1, padx=0, pady=10)


        self.InnerFrameCustomer2 = tk.Frame(self,  bg = "#2D2B55", width = 550, height = 550) 
        self.InnerFrameCustomer2.pack(side="bottom",fill="y")


        table = ttk.Treeview(self.InnerFrameCustomer2,columns=("CustomerID","Name","Email","Phone"), show="headings",height=10)
        table.heading("CustomerID",text="CustomerID")
        table.heading("Name", text="Name")
        table.heading("Email", text="Email")
        table.heading("Phone", text="Phone")
        table.column("CustomerID",width=75, anchor="w")
        table.column("Name", width=130, anchor="w")
        table.column("Email", width=150, anchor="w")
        table.column("Phone", width=120, anchor="w")
        table.place(relx =0.45,rely =0.5, anchor="center")

    

        #-------------------------Function Area--------------------------
        def DeleteEntry():
            Enter_ID.delete(0, tk.END)
            Enter_Name.delete(0, tk.END)
            Enter_Email.delete(0, tk.END)
            Enter_Phone.delete(0, tk.END)
            

        def on_select(event):
            global selected_id
            focus = table.focus()
            if not focus: return
            vals = table.item(focus)["values"]
            if vals:
                selected_id = vals[0]
                id_var.set(vals[0])
                name_var.set(vals[1])
                email_var.set(vals[2])
                phone_var.set(vals[3])
            else:
                selected_id = None
        table.bind("<<TreeviewSelect>>", on_select)

        def add():
            id = Enter_ID.get()
            name = Enter_Name.get()
            email = Enter_Email.get()
            phone = Enter_Phone.get()
            add_to_table(table,id,name,email,phone)
            DeleteEntry()
        def update():
            Update(table,name_var,email_var,phone_var,id_var,selected_id)
            DeleteEntry()
        def delete():
            Delete(table)
            DeleteEntry()

        AddButton = tk.Button(InnerFrameCustomer1Ver3, text="Add",width=10,command=add,bg="#A599E9")
        AddButton.grid(row=2, column=1, padx=10, pady=10)

        UpdateButton = tk.Button(InnerFrameCustomer1Ver3,text="Update", width=10, command=update,bg="#A599E9")
        UpdateButton.grid(row=3, column=1, padx=10, pady=10)

        DeleteButton = tk.Button(InnerFrameCustomer1Ver3,text="Delete", width=10, command=delete,bg="#A599E9")
        DeleteButton.grid(row=4, column=1, padx=10, pady=10)

    

        load(table)

import tkinter as tk
from tkinter import ttk
from sql import loadVehicleJoin, CustomerForm
from datetime import date
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Car Rentals and Services")
root.resizable(False,False)
root.configure(bg="#2D2B55")
root.geometry("650x500")

TopFrame = tk.Frame(root,bg="red",width=650, height=500)
TopFrame.place(relx=0.5, rely=0.0, anchor="n")
TitleLabel = tk.Label(TopFrame, text="CUSTOMER FORM",bg="#2D2B55",fg="#A599E9",font=("Arial",10,"bold")).pack()
#2D2B55 - normal purple
#1E1E3F -  dark purple
#FAD000 - golden
#A599E9 - foreground

img = Image.open(r"C:\Users\User\Downloads\car.png")
img = img.resize((30,30))
tk_img = ImageTk.PhotoImage(img)
label = tk.Label(root, image=tk_img, bg="#2D2B55")
label.image = tk_img
label.place(relx=0.05, rely = 0.05, anchor = tk.CENTER)
titlelabel = tk.Label(root, text="CAR RENTALS AND SERVICES", fg="#FAD000",bg="#2D2B55").place(relx=0.1999, rely = 0.05, anchor = tk.CENTER)

CustomerFrame = tk.Frame(root, bg="#2D2B55",highlightbackground="#1E1E3F",highlightthickness=1,highlightcolor="#FAD000")
CustomerFrame.place(relx=0.16, rely = 0.32, anchor ="center")

labelName = tk.Label(CustomerFrame,bg="#2D2B55", text="Name",fg="white") 
labelName.grid(row=0, column=0, padx=0, pady=10, sticky="e")

CustomerName = tk.Entry(CustomerFrame, width=20)
CustomerName.grid(row=0, column=1, padx=0, pady=10)

labelEmail = tk.Label(CustomerFrame,bg="#2D2B55", text="Email",fg="white")
labelEmail.grid(row=1, column=0, padx=0, pady=10, sticky="e")

CustomerEmail = tk.Entry(CustomerFrame, width=20)
CustomerEmail.grid(row=1, column=1, padx=0, pady=10)

labelPhone = tk.Label(CustomerFrame,bg="#2D2B55", text="Phone",fg="white")
labelPhone.grid(row=2, column=0, padx=0, pady=10, sticky="e")

CustomerPhone = tk.Entry(CustomerFrame, width=20)
CustomerPhone.grid(row=2, column=1, padx=0, pady=10)

Label = tk.Label(CustomerFrame, text="",bg="#2D2B55",fg="white").grid(row=3, column=3, padx=15, pady=10)
Label = tk.Label(CustomerFrame, text="Customer Information",bg="#2D2B55",fg="white").grid(row=4, column=1, padx=0, pady=10)


TransactionFrame = tk.Frame(root, bg="#2D2B55",highlightbackground="#1E1E3F",highlightthickness=1,highlightcolor="#FAD000")
TransactionFrame.place(relx=0.50, rely = 0.32, anchor ="center")

LayoutPaymentMethod = tk.Label(TransactionFrame,bg="#2D2B55", text="Pay Method",fg="white")
LayoutPaymentMethod.grid(row=0, column=0, padx=0, pady=10, sticky="e")

TransactionPaymentMethod = ttk.Combobox(TransactionFrame, width=18)
TransactionPaymentMethod.grid(row=0, column=1, padx=0, pady=10)
TransactionPaymentMethod['values'] = ['Credit Card','Cash','Debit Card','Bank Transfer','GCash']
labelAmount = tk.Label(TransactionFrame,bg="#2D2B55", text="Amount",fg="white")
labelAmount.grid(row=1, column=0, padx=0, pady=10, sticky="e")

TransactionAmount = tk.Entry(TransactionFrame, width=20)
TransactionAmount.grid(row=1, column=1, padx=0, pady=10)

LayoutRentalDate = tk.Label(TransactionFrame,bg="#2D2B55", text="Rental Date",fg="white")
LayoutRentalDate.grid(row=2, column=0, padx=0, pady=10, sticky="e")

Enter_RentalDate = tk.Entry(TransactionFrame, width=20)
Enter_RentalDate.grid(row=2, column=1, padx=0, pady=10)

ReturnDate = tk.Label(TransactionFrame,bg="#2D2B55", text="Return Date",fg="white") 
ReturnDate.grid(row=3, column=0, padx=0, pady=10, sticky="e")

Enter_ReturnDate = tk.Entry(TransactionFrame, width=20)
Enter_ReturnDate.grid(row=3, column=1, padx=0, pady=10)

Label = tk.Label(TransactionFrame, text="",bg="#2D2B55",fg="white").grid(row=3, column=3, padx=13, pady=0)
Label = tk.Label(TransactionFrame, text="Transaction Information",bg="#2D2B55",fg="white").grid(row=5, column=1, padx=0, pady=10)

VehicleFrame = tk.Frame(root, bg="#2D2B55",highlightbackground="#1E1E3F",highlightthickness=1,highlightcolor="#FAD000")
VehicleFrame.place(relx=0.84, rely = 0.321, anchor ="center")

VehName = tk.Label(VehicleFrame,bg="#2D2B55", text="Vehicle",fg="white")
VehName.grid(row=0, column=0, padx=0, pady=10, sticky="e")

vehiclename_var = tk.StringVar()
cost_var = tk.StringVar()

VehicleName = tk.Entry(VehicleFrame, width=20,textvariable=vehiclename_var)
VehicleName.grid(row=0, column=1, padx=0, pady=11)

labelPrice = tk.Label(VehicleFrame,bg="#2D2B55", text="Cost",fg="white") 
labelPrice.grid(row=1, column=0, padx=0, pady=10, sticky="e")

Vehicle = tk.Entry(VehicleFrame, width=20, textvariable=cost_var)
Vehicle.grid(row=1, column=1, padx=0, pady=11)

Label = tk.Label(VehicleFrame, text="",bg="#2D2B55",fg="white").grid(row=2, column=3, padx=12, pady=30)
Label = tk.Label(VehicleFrame, text="Vehicle Information",bg="#2D2B55",fg="white").grid(row=3, column=1, padx=0, pady=10)

def clear():
    CustomerName.delete(0, tk.END)  
    CustomerEmail.delete(0, tk.END)  
    CustomerPhone.delete(0, tk.END)  
    TransactionPaymentMethod.delete(0, tk.END)  
    TransactionAmount.delete(0, tk.END)  
    Enter_RentalDate.delete(0, tk.END)  
    Enter_ReturnDate.delete(0, tk.END)  
    VehicleName.delete(0, tk.END)  
    Vehicle.delete(0, tk.END) 

def add():
 
    name = CustomerName.get() 
    email = CustomerEmail.get()
    phone = CustomerPhone.get()
    paymethod = TransactionPaymentMethod.get()
    paymentdate = date.today()
    amount = TransactionAmount.get()
    rentaldate = Enter_RentalDate.get()
    returndate = Enter_ReturnDate.get()
    model = VehicleName.get()
    CustomerForm(name,email,phone,paymethod,paymentdate,amount,rentaldate,returndate,model)
    clear()
   

Submit = tk.Button(root, text="Submit",borderwidth = 2, highlightthickness=0,bg="#1E1E3F",fg="white",highlightcolor="goldenrod",highlightbackground="black",command=add).place(relx=0.87, rely = 0.92, anchor ="center")
Clear = tk.Button(root, text="Clear",command=clear,borderwidth = 2, highlightthickness=0,bg="#1E1E3F",fg="white",highlightcolor="goldenrod",highlightbackground="black").place(relx=0.94, rely = 0.92, anchor ="center")

style = ttk.Style()
style.theme_use("default")
labelTable = tk.Label(root,text="Select a Vehicle",bg="#2D2B55",fg="white").place(relx =0.26,rely =0.59, anchor="center")
table = ttk.Treeview(root,columns=("Vehicle","Type","Rental Cost"), show="headings",height=7)
table.heading("Vehicle",text="Vehicle")
table.heading("Type",text="Type")
table.heading("Rental Cost", text="Rental Cost")
table.column("Vehicle",width=130, anchor="w")
table.column("Type",width=130, anchor="w")
table.column("Rental Cost", width=130, anchor="w")
table.place(relx =0.50,rely =0.78, anchor="center")



def on_select(event):
        global selected_id
        focus = table.focus()
        if not focus: return
        vals = table.item(focus)["values"]
        if vals:
            selected_id = vals[0]
            vehiclename_var.set(vals[0])
            cost_var.set(vals[2])
        else:
            selected_id = None
table.bind("<<TreeviewSelect>>", on_select)

loadVehicleJoin(table)
root.mainloop()
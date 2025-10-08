import mysql.connector
from tkinter import messagebox 
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database="carrentalsandservices"
)

if db.is_connected():
    print("Successfully connected to MySSQL!")

cursor = db.cursor()  


cursor.execute("SELECT * FROM customer")
rows = cursor.fetchall()
def reports(table):
    cursor.execute("select customer.name, payment.paymentmethod, payment.amount, rental.rentaldate, vehicle.totalcost, vehicle.model from customer inner join rental on customer.customerid = rental.customerid inner join vehicle on rental.vehicleid = vehicle.vehicleid inner join payment on rental.rentalid = payment.rentalid")
    rows = cursor.fetchall()
    for row in rows:
        table.insert("","end",values=row) 

def CustomerForm(name,email,phone,paymethod,paymentdate,amount,rentaldate,returndate,model):
    answer = messagebox.askyesno("Confirm","Do you want to rent a vehicle?")
    if answer:
        print("Customer proceeds...")
        cursor.execute("INSERT INTO customer (name,email,phone) values (%s,%s,%s)",(name,email,phone))
        db.commit()
        cursor.execute("SELECT customerid from customer where name = %s",(name,))
        customerid = cursor.fetchone()
        cursor.execute("SELECT vehicleid from vehicle where model = %s",(model,))
        vehicleid = cursor.fetchone()
        if customerid and vehicleid:
            customerid = customerid[0]
            vehicleid = vehicleid[0]
            cursor.execute("INSERT INTO rental (rentaldate,returndate,customerid,vehicleid) VALUES (%s,%s,%s,%s)",(rentaldate,returndate,customerid,vehicleid))
            db.commit()

            cursor.execute("SELECT rentalid from rental where customerid = %s",(customerid,))
            rentalid = cursor.fetchone()
            if rentalid:
                rentalid = rentalid[0]
                cursor.execute("INSERT INTO payment (paymentmethod,paymentdate,amount,rentalid) VALUES (%s,%s,%s,%s)",(paymethod,paymentdate,amount,rentalid))
                db.commit()
        
        print("Customer transaction success!")
    else:
        print("Customer cancels...")

def loadVehicleJoin(table):
    for items in table.get_children():
         table.delete(items)
    cursor.execute("select vehicle.Model, vehicle.type, vehicle.totalcost from vehicle order by vehicle.vehicleid asc")
    rows = cursor.fetchall()
    for row in rows:
        table.insert("","end",values=row)   

def load(table):
    for items in table.get_children():
         table.delete(items)
    cursor.execute("SELECT CustomerID, Name, Email, Phone FROM customer")
    rows = cursor.fetchall()
    for row in rows:
        table.insert("","end",values=row) 


def loadPayment(tablePayment):
    for items in tablePayment.get_children():
         tablePayment.delete(items)
    cursor.execute("SELECT PaymentID, PaymentMethod, PaymentDate, Amount, RentalID FROM payment")
    rowsPayment = cursor.fetchall()
    for row in rowsPayment:
        tablePayment.insert("","end",values=row)  
def loadRentals(tableRentals):
    for items in tableRentals.get_children():
         tableRentals.delete(items)
    cursor.execute("SELECT RentalID,RentalDate,ReturnDate,CustomerID,VehicleID FROM rental")
    rowsRentals = cursor.fetchall()
    for row in rowsRentals:
        tableRentals.insert("","end",values=row) 
def loadVehicle(tableVehicle):
    for items in tableVehicle.get_children():
         tableVehicle.delete(items)
    cursor.execute("SELECT VehicleID, Type, Make, Model, totalCost FROM Vehicle")
    rowsVehicle = cursor.fetchall()
    for row in rowsVehicle:
        tableVehicle.insert("","end",values=row)

def add_to_table(table,id,name,email,phone): 
    answer = messagebox.askokcancel("Confirm","Do you want to add data?")
    if answer:
            if name and id:
                table.insert("","end", values=(id, name))
        
                insert_statement = '''INSERT INTO customer VALUES (%s, %s, %s, %s)'''
                values_to_insert = (id,name,email,phone)
                cursor.execute(insert_statement,values_to_insert)
                print("Data added successfully!*")
                
                db.commit()
                load(table)
            return id, name, email, phone
    else:
        print("Customer cancels...")
def add_to_table1(tablePayment,id,method,payment,amount,rental): 
    answer = messagebox.askokcancel("Confirm","Do you want to add data?")
    if answer:
            if method and id:
                tablePayment.insert("","end", values=(id, method))
        
                insert_statement = '''INSERT INTO Payment VALUES (%s, %s, %s, %s, %s)'''
                values_to_insert = (id,method,payment,amount,rental)
                cursor.execute(insert_statement,values_to_insert)
                print("Data added successfully!*")

                
                db.commit()
                loadPayment(tablePayment)
            return id,method,payment,amount,rental
    else:
        print("Customer cancels...")
def  add_to_table2(tableRentals,id,rentalDate,returnDate,customerid,vehicleid):
    answer = messagebox.askokcancel("Confirm","Do you want to add data?")
    if answer:
            if rentalDate and id:
                tableRentals.insert("","end", values=(id, rentalDate))
        
                insert_statement = '''INSERT INTO rental VALUES (%s, %s, %s, %s, %s, %s)'''
                values_to_insert = (id,rentalDate,returnDate,customerid,vehicleid)
                cursor.execute(insert_statement,values_to_insert)
                print("Data added successfully!*")

                db.commit()
                loadRentals(tableRentals)
            return id,rentalDate,returnDate,customerid,vehicleid
    else:
        print("Customer cancels...")
def  add_to_table3(tableVehicle,id,types,make,model,totalcost):
    answer = messagebox.askokcancel("Confirm","Do you want to add data?")
    if answer:
            if types and id:
                tableVehicle.insert("","end", values=(id, types))
        
                insert_statement = '''INSERT INTO vehicle VALUES (%s, %s, %s, %s,%s)'''
                values_to_insert = (id,types,make,model,totalcost)
                cursor.execute(insert_statement,values_to_insert)
                print("Data added successfully!*")

                db.commit()
                loadVehicle(tableVehicle)
            return id,types,make,model,totalcost
    else:
        print("Customer cancels...")
def Delete(table):
    answer = messagebox.askokcancel("Confirmation","Are you sure you want to delete this row?")
    if answer:
        select_item = table.focus()
        value = table.item(select_item)["values"][0]
        cursor.execute("Delete from customer where CustomerID = %s",[value])
        db.commit()
        print("Deleted successful",value)
        load(table)
    else:
        print("Customer cancels...")
def Delete1(tablePayment):
    answer = messagebox.askokcancel("Confirmation","Are you sure you want to delete this row?")
    if answer:
        select_item = tablePayment.focus()
        value = tablePayment.item(select_item)["values"][0]
        cursor.execute("Delete from Payment where PaymentID = %s",[value])
        db.commit()
        print("Deleted successful",value)
        loadPayment(tablePayment)
    else:
        print("Customer cancels...")
def Delete2(tableRentals):
    answer = messagebox.askokcancel("Confirmation","Are you sure you want to delete this row?")
    if answer:
        select_item = tableRentals.focus()
        value = tableRentals.item(select_item)["values"][0]
        cursor.execute("Delete from rental where RentalID = %s",[value])
        db.commit()
        print("Deleted successful",value)
        loadRentals(tableRentals)
    else:
        print("Customer cancels...")
def Delete3(tableVehicle):
    answer = messagebox.askokcancel("Confirmation","Are you sure you want to delete this row?")
    if answer:
        select_item = tableVehicle.focus()
        value = tableVehicle.item(select_item)["values"][0]
        cursor.execute("Delete from vehicle where VehicleID = %s",[value])
        db.commit()
        print("Deleted successful",value)
        loadVehicle(tableVehicle)
    else:
        print("Customer cancels...")
def Update(table,name_var,email_var,phone_var,id_var,selected_id):
    answer = messagebox.askokcancel("Confirmation","Are you sure you want to delete this row?")
    if answer:
        if selected_id:
            cursor.execute("UPDATE customer set CustomerID = %s, Name = %s, Email = %s, Phone = %s WHERE CustomerID = %s",(id_var.get(),name_var.get(),email_var.get(),phone_var.get(),id_var.get()))
            db.commit()
        else:
            print("No row selected")
        load(table)
    else:
        print("Customer cancels...")

def Update1(tablePayment,paymentid_var,paymentMethod_var,Date_var,amount_var,rental_var,selected_id):
    answer = messagebox.askokcancel("Confirmation","Are you sure you want to delete this row?")
    if answer:
        if selected_id:
            cursor.execute("UPDATE Payment set PaymentID = %s, PaymentMethod = %s, PaymentDate = %s, Amount = %s, RentalID = %s WHERE PaymentID = %s",(paymentid_var.get(),paymentMethod_var.get(),Date_var.get(),amount_var.get(),rental_var.get(),paymentid_var.get()))
            db.commit()
        else:
            print("No row selected")
        loadPayment(tablePayment)
    else:
        print("Customer cancels...")
def Update2(tableRentals,rentalid_var,rentaldate_var,returndate_var,customerid_var,vehicleid_var,selected_id):
    answer = messagebox.askokcancel("Confirmation","Are you sure you want to delete this row?")
    if answer:
        if selected_id:
            cursor.execute("UPDATE rental set RentalID = %s, RentalDate = %s, ReturnDate = %s, CustomerID = %s, VehicleID = %s WHERE RentalID = %s",(rentalid_var.get(),rentaldate_var.get(),returndate_var.get().get(),customerid_var.get(),vehicleid_var.get(),rentalid_var.get()))
            db.commit()
        else:
            print("No row selected")
        loadRentals(tableRentals)
    else:
        print("Customer cancels...")
def Update3(tableVehicle,type_var,make_var,model_var,vehicleid_var,totalcost_var,selected_id):
    answer = messagebox.askokcancel("Confirmation","Are you sure you want to delete this row?")
    if answer:
        if selected_id:
            cursor.execute("UPDATE vehicle set VehicleID = %s, Type = %s, Make = %s, Model = %s, totalcost = %s WHERE VehicleID = %s",(vehicleid_var.get(),type_var.get(),make_var.get(),model_var.get(),totalcost_var.get(),vehicleid_var.get()))
            db.commit()
        else:
            print("No row selected")
        loadVehicle(tableVehicle)
    else:
        print("Customer cancels...")






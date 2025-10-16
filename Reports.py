import tkinter as tk
from tkinter import ttk
from sql import reports
class ReportFrame(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        
        self.label = tk.Label(self, text="History", bg="#2D2B55",fg="#FAD000")
        self.label.pack()

        table = ttk.Treeview(self,columns=("Name","PayMethod","Amount","RentalDate","Cost","Vehicle"), show="headings",height=45)
        table.heading("Name",text="Name")
        table.heading("PayMethod", text="PayMethod")
        table.heading("Amount", text="Amount")
        table.heading("RentalDate", text="RentalDate")
        table.heading("Cost", text="Cost")
        table.heading("Vehicle", text="Vehicle")

        table.column("Name",width=120, anchor="w")
        table.column("PayMethod", width=100, anchor="w")
        table.column("Amount", width=100, anchor="w")
        table.column("RentalDate", width=100, anchor="w")
        table.column("Cost", width=100, anchor="w")
        table.column("Vehicle", width=120, anchor="w")
        table.place(relx =0.475,rely =0.9999, anchor="center")


        reports(table)
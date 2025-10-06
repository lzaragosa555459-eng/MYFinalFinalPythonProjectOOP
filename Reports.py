import tkinter as tk
from tkinter import ttk
from sql import reports
class ReportFrame(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        
        self.label = tk.Label(self, text="History", bg="#2D2B55",fg="#FAD000")
        self.label.pack()

        table = ttk.Treeview(self,columns=("Name","PayMethod","Amount","RentalDate","Cost","Vehicle"), show="headings",height=15)
        table.heading("Name",text="Name")
        table.heading("PayMethod", text="PayMethod")
        table.heading("Amount", text="Amount")
        table.heading("RentalDate", text="RentalDate")
        table.heading("Cost", text="Cost")
        table.heading("Vehicle", text="Vehicle")

        table.column("Name",width=70, anchor="w")
        table.column("PayMethod", width=90, anchor="w")
        table.column("Amount", width=70, anchor="w")
        table.column("RentalDate", width=75, anchor="w")
        table.column("Cost", width=70, anchor="w")
        table.column("Vehicle", width=100, anchor="w")
        table.place(relx =0.45,rely =0.39, anchor="center")


        reports(table)
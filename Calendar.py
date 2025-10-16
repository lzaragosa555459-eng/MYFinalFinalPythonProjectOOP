import tkinter as tk
from tkinter import ttk

def setCalendar(entry,parent):
    root = tk.Toplevel(parent)
    root.title("Calendar")
    root.geometry("200x100+600+300")
    root.resizable(False,False)

    def setLabelDate():
        getYear = Year.get()
        getMonth = int(Month.current())+1
        getDay = int(Day.get())
        if getDay > 9:
            if getMonth > 9:
                entry.insert(tk.END, f"{getYear}-{getMonth}-{getDay}")
            elif getMonth < 9:
                entry.insert(tk.END, f"{getYear}-0{getMonth}-{getDay}")
        elif getDay < 10: 
            if getMonth < 10:
                entry.insert(tk.END, f"{getYear}-0{getMonth}-0{getDay}")
            elif getMonth > 10:
                entry.insert(tk.END, f"{getYear}-{getMonth}-0{getDay}")
        root.destroy()

    

    label = tk.Label(root,text="Year")
    label.grid(row=0,column=0,padx=0,pady=(20,0),sticky='w')
    Year = ttk.Combobox(root,width=10)
    Year['value'] = tuple(range(2000,2031))
    Year.grid(row=0,column=1,padx=0,pady=(20,0))

    label = tk.Label(root,text="Month")
    label.grid(row=1,column=0,padx=0,pady=0,sticky='w')
    Month = ttk.Combobox(root, width=10)
    Month['value'] = ['January','Febuary','March','April','May','June','July','August','September','October','November','December']
    Month.grid(row=1,column=1,padx=0,pady=0)

    label = tk.Label(root,text="Day")
    label.grid(row=2,column=0,padx=0,pady=0,sticky='w')
    Day = ttk.Combobox(root,width=10)
    Day['value'] = tuple(range(1,10)) + tuple(range(10,32))
    Day.grid(row=2,column=1,padx=0,pady=0)




    button = tk.Button(root,text="Set", command=setLabelDate)
    button.place(relx=0.85,rely=0.70,anchor='center')

    root.mainloop() 
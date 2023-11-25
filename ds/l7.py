import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("Simple Calculator")
root.geometry("500x300")

Calci = ttk.Frame(root, padding = "50 50 50 50")
Calci.pack()

no1Label = ttk.Label(Calci, text = "Enter first no: ")
no1Label.grid(column=0,row=0)
no1 = tk.StringVar()
ttk.Entry(Calci, width=25, textvariable=no1).grid(column=1,row=0)

no2Label = ttk.Label(Calci, text = "Enter second no: ")
no2Label.grid(column=0,row=1)
no2 = tk.StringVar()
ttk.Entry(Calci, width=25, textvariable=no2).grid(column=1,row=1)

def add():
 num1 = float(no1.get())
 num2 = float(no2.get())
 res.set(num1+num2)
 
def sub():
 num1 = float(no1.get())
 num2 = float(no2.get())
 res.set(num1-num2)
 
def mul():
 num1 = float(no1.get())
 num2 = float(no2.get())
 res.set(num1*num2)

def div():
 num1 = float(no1.get())
 num2 = float(no2.get())
 if num2 == 0:
  res.set("Divide by zero error")
 else:
  res.set(num1/num2)
 

ttk.Button(Calci, text = "Add", command=add).grid(column=0, row=2)
ttk.Button(Calci, text = "Sub", command=sub).grid(column=1, row=2)
ttk.Button(Calci, text = "Mul", command=mul).grid(column=0, row=3)
ttk.Button(Calci, text = "Div", command=div).grid(column=1, row=3)

res = tk.StringVar()
no5Label = ttk.Label(Calci, text = "Result: ")
no5Label.grid(column=0,row=4)
ttk.Entry(Calci, width=25, textvariable=res, state="readonly").grid(column=1,row=4)

for child in Calci.winfo_children():
 child.grid_configure(padx = 5, pady = 5)

root.mainloop()
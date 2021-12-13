import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

main_window = tk.Tk()
main_window.title('Employee Management System')
connection = sqlite3.connect('emp.db')

table_name = "Employee_Table"
theirid = "Employee_ID"
theirname = "Employee_Name"
theirdepartment = "Employee_Department"
theiraddress = "Employee_Address"
theirphone = "Employee_Phone"
connection.execute("CREATE TABLE IF NOT EXISTS "+table_name+"("+theirid + " INTEGER PRIMARY KEY AUTOINCREMENT,"+theirname+"TEXT,"+theirdepartment+"TEXT,"+theiraddress+"TEXT,"+theirphone+"INTEGER)")

onelabel = tk.Label(main_window, text='Employees Records Over Here', fg='black', width=35)
onelabel.config(font=('arial', 30))
onelabel.grid(row=0, columnspan=2, padx=(10, 10), pady=(30, 0))


class Employee:
    theirName = ""
    theirDepartment = ""
    theirAddress = ""
    theirPhone = 0
    def __init__(self, theirName, theirDepartment, theirAddress, theirPhone):
        self.theirName = theirName
        self.theirDepartment = theirDepartment
        self.theirAddress = theirAddress
        self.theirPhone = theirPhone

namelabel = tk.Label(main_window, text="Enter Your Name ", width=40, anchor='w', font=('arial', 12)).grid(row=1, column=0,padx=(10,0), pady=(30,0))
departmentlabel = tk.Label(main_window, text="Enter Your Department's Name ", width=40, anchor='w', font=('arial', 12)).grid(row=2, column=0,padx=(10,0), pady=(30,0))
addresslabel = tk.Label(main_window, text="Enter Your Address ", width=40, anchor='w', font=('arial', 12)).grid(row=3, column=0,padx=(10,0), pady=(30,0))
phonelabel = tk.Label(main_window, text="Enter Your Phone Number ", width=40, anchor='w', font=('arial', 12)).grid(row=4, column=0,padx=(10,0), pady=(30,0))

nameentry = tk.Entry(main_window, width=30)
departmententry = tk.Entry(main_window, width=30)
addressentry = tk.Entry(main_window, width=30)
phoneentry = tk.Entry(main_window, width=30)
nameentry.grid(row=1,column=1,padx=(0,10),pady=(30,20))
departmententry.grid(row=2,column=1,padx=(0,10),pady=20)
addressentry.grid(row=3,column=1,padx=(0,10),pady=20)
phoneentry.grid(row=4,column=1,padx=(0,10),pady=20)



def get_input():
  global list
  global nameentry, departmententry, addressentry, phoneentry
  global table_name, theirname, theirdepartment, theiraddress, theirphone
  username = nameentry.get()
  nameentry.delete(0, tk.END)
  department=departmententry.get()
  departmententry.delete(0, tk.END)
  place=addressentry.get()
  addressentry.delete(0, tk.END)
  number=phoneentry.get()
  phoneentry.delete(0, tk.END)
  connection.execute("INSERT INTO "+table_name+"("+theirname+", "+theirdepartment+", "+theiraddress+", "+theirphone+") VALUES("+username+", "+department+", "+place+", "+number+")")

connection.commit()
messagebox.showinfo("Saving Data","Your Data is Successfully Saved.")

def finish_window():
  main_window.destroy()
  second_window=tk.Tk()
  second_window.title("Available Records")
  labeltwo=tk.Label(second_window, text="Records of Employee", fg='black', width=40)
  labeltwo.config(font=("arial", 30))
  labeltwo.pack()

  tree=ttk.Treeview(second_window)
  tree["columns"]=("one","two","three","four")
  tree.heading("one",text="Name of Employee")
  tree.heading("two",text="Department Name")
  tree.heading("three",text="Address")
  tree.heading("four",text="Phone Number")

  cursor=connection.execute("SELECT * FROM "+table_name+";")
  i = 0
  for row in cursor:
    tree.insert("",i,text='Employee'+str(row[0]),values=(row[1],row[2],row[3],row[4]))
    i=i+1
  tree.pack()
  second_window.mainloop()


button1 = tk.Button(main_window, text='Enter Records',command=lambda: get_input())
button1.grid(row=5, column=0, pady=20)
button2 = tk.Button(main_window, text='Display Records',command=lambda: finish_window())
button2.grid(row=6, column=0)


main_window.mainloop()

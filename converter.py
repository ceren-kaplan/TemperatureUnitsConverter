import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()

window_height = 280
window_width = 350

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
root.resizable(False, False)
root.title("Temperature Units Converter")

 

def clear():
    entry_result.configure(state="normal")
    entry.delete(0,"end")
    entry_result.delete(0,"end")
    unit_from.set("")
    unit_to.set("")
    entry.focus()
    entry_result.configure(state="disabled")
  

def convert():
    entry_result.configure(state="normal")
    entry_result.delete(0,"end")
    data=entry.get()
    selected_unit_to=selected_to.get()
    selected_unit_from=selected_from.get()  
   
    
    if((data=="") or (selected_unit_to=="" ) or (selected_unit_from=="" )):
        entry_result.configure(state="disabled")
        msg = "Please fill in all fields!"
        showinfo(title='Warning',message=msg)        
            
    else:
        try:
            float(data)   
        except ValueError:
             entry_result.configure(state="disabled")
             msg2 = "Please enter a numeric value!"
             showinfo(title='Warning',message=msg2)
             entry.delete(0,"end")
             entry.focus()             
        else:
            if(selected_unit_to==selected_unit_from):
                entry_result.insert(0,data)
            elif((selected_unit_from=="Celsius") and (selected_unit_to=="Kelvin")):
                Kelvin=float(data)+273.15
                entry_result.insert(0,Kelvin)
            elif((selected_unit_from=="Celsius") and (selected_unit_to=="Fahrenheit")):
                Fahrenheit=(float(data)*9/5)+32
                entry_result.insert(0,Fahrenheit)
            elif((selected_unit_from=="Kelvin") and (selected_unit_to=="Celsius")):
                Celsius=(float(data) - 273.15)
                entry_result.insert(0,Celsius)
            elif((selected_unit_from=="Kelvin") and (selected_unit_to=="Fahrenheit")):
                Fahrenheit=(float(data)-273.15)*9/5+32
                entry_result.insert(0,Fahrenheit)
            elif((selected_unit_from=="Fahrenheit") and (selected_unit_to=="Celsius")):
                Celsius=5/9*(float(data)-32)
                entry_result.insert(0,Celsius)
            elif((selected_unit_from=="Fahrenheit") and (selected_unit_to=="Kelvin")):
                Kelvin=5/9*(float(data)-32)+273.15
                entry_result.insert(0,Kelvin)
            entry_result.configure(state="disabled")
          
                         
 

units = ("Celsius", "Kelvin", "Fahrenheit")

selected_from= tk.StringVar()
selected_to= tk.StringVar()

label_from=tk.Label(text="From The Unit : ",font="Arial 10 ",fg="purple")
label_from.place(x=20,y=65)
label_to=tk.Label(text="To The Unit :",font="Arial 10 ",fg="purple")
label_to.place(x=20,y=95)
label_value=tk.Label(text="Value To Convert: ",font="Arial 10 ",fg="purple")
label_value.place(x=20,y=35)

unit_from= ttk.Combobox(root, textvariable=selected_from)
unit_from['values'] = units
unit_from['state'] = 'readonly' 
unit_from.place(x=130,y=65,width=200)
unit_to = ttk.Combobox(root, textvariable=selected_to)
unit_to['values'] = units
unit_to['state'] = 'readonly'  
unit_to.place(x=130,y=95,width=200)

entry=tk.Entry(root)
entry.place(x=130, y=37,width=200)
entry_result=tk.Entry(root)
entry_result.place(x=20, y=200,width=310)
entry_result.configure(state="disabled")

button_convert=tk.Button(root)
button_convert.config(text="Convert",bg="green",fg="white",command=convert)
button_convert.place(x=20,y=140,width=140)
button_clear=tk.Button(root)
button_clear.config(text="Clear",bg="red",fg="white",command=clear)
button_clear.place(x=190,y=140,width=140)

root.mainloop()

import tkinter as tk

def SI():
    p = float(entry.get())
    r = float(entry1.get())
    t = float(entry2.get())
    SI = (p * r * t) / 100
    result.config(text=f"Simple Interest : {SI}").place(x=10,y=210)
    result.place(x=10,y=250)

def CI():
    p = float(entry.get())
    r = float(entry1.get())
    t = float(entry2.get())
    SI = (p * r * t) / 100
    CI=p+SI
    result.config(text=f"compound Interest : {CI}").place(x=10,y=210)
    result.place(x=10,y=250)
    
def reset():
    entry.delete(0, tk.END)
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result.config(text="")
    
root = tk.Tk()
root.geometry("300x300")
root.title("SI & CI Calculator")
root.config(bg="white")

l = tk.Label(root, text="Calculator",bg='white')
l.place(x=100, y=5)

label = tk.Label(root, text="Principle : ",bg='white')
label.place(x=10, y=25)
entry = tk.Entry(root)
entry.place(x=80, y=25)

label1 = tk.Label(root, text="Rate : ",bg='white')
label1.place(x=30, y=55)
entry1 = tk.Entry(root)
entry1.place(x=80, y=55)

label2 = tk.Label(root, text="Time : ",bg='white')
label2.place(x=30, y=85)
entry2 = tk.Entry(root)
entry2.place(x=80, y=85)

result = tk.Label(root, text="",bg='white')
result.place(x=10, y=145)

button = tk.Button(root, text="Simple Interest", command=SI, bg='white')
button.place(x=10, y=115)

button1 = tk.Button(root, text="Compound Interest", command=CI ,bg='white')
button1.place(x=140, y=115)

button2 = tk.Button(root, text="Reset", command=reset, bg='white')
button2.place(x=100, y=150)


result = tk.Label(root, text="" ,bg='white')
result.place(x=10, y=190)
root.mainloop()

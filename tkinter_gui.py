import tkinter as tk
root=tk.Tk()
root.geometry("200x300")
root.title("EDUYEAR")
root.configure(bg="black")
e1=tk.Text(root)
l1=tk.Label(root,text="Output:")
l1.place(x=10,y=5)
e1.place(x=10,y=35,height=50,width=180)
e2=tk.Text(root)
l=tk.Label(root,text="-----------------------------------")
l.place(x=10,y=90)
l=tk.Label(root,text="You said:")
l.place(x=10,y=120)
e2.place(x=10,y=150,height=30,width=180)
b1=tk.Button(root,text="Speak",bg="red",fg="white",command=check)
b1.place(x=50,y=200,height=50,width=100)

root.mainloop()
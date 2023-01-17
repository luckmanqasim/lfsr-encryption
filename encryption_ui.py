from tkinter import *
from tkinter import ttk
from encryption import *

root = Tk()
root.title("LFSR Encrytpion")
frm = ttk.Frame(root, padding=10)
frm.grid()

name_var = StringVar()
seed_var = StringVar()
k_var = IntVar()

def submit():
    name = name_var.get()
    seed = list(seed_var.get())
    seed_list = [eval(i) for i in seed]
    k = int(k_var.get())

    ans = encrypt(name, seed_list, k)
    ansl.config(text=ans)

    name_var.set(name)


title = ttk.Label(frm, text="Base64 Text Encryption using LFSR", font="Verdana")
name_label = ttk.Label(frm, text="Enter your text:", font="Verdana")
name_entry = ttk.Entry(frm, textvariable=name_var, width=40)
seed_label = ttk.Label(frm, text="Enter your seed:", font="Verdana")
seed_entry = ttk.Entry(frm, textvariable=seed_var, width=40)
k_label = ttk.Label(frm, text="Enter your tap position:", font="Verdana")
k_entry = ttk.Entry(frm, textvariable=k_var, width=40)
sub_btn = ttk.Button(frm, text="Submit", command=submit)
ans_label = ttk.Label(frm, text="Encrypted text: ", font="Verdana")
ansl = ttk.Label(frm, text="", font="Verdana")

title.grid(column=0, row=0, padx=4, pady=2, columnspan=3)
name_label.grid(column=0, row=1, padx=4, pady=2)
name_entry.grid(column=0, row=2, padx=4, pady=2)
seed_label.grid(column=1, row=1, padx=4, pady=2)
seed_entry.grid(column=1, row=2, padx=4, pady=2)
k_label.grid(column=2, row=1, padx=4, pady=2)
k_entry.grid(column=2, row=2, padx=4, pady=2)
sub_btn.grid(column=0, row=3, padx=4, pady=2, columnspan=3)
ans_label.grid(column=0, row=4, padx=4, pady=2)
ansl.grid(column=1, row=4, padx=4, pady=2, columnspan=2)

root.mainloop()
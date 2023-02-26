from tkinter import *
from tkinter import ttk

root = Tk()
root.title("BTC")
root.geometry("700x500+500+200")
root.maxsize(1000,700)

def translate():
    try:
        int(input.get())
        if int(input.get()[-1]) > 1:
            input.delete(len(input.get())-1, END)
            return
    except:
        input.delete(0,END)
        return
    bin = input.get()
    if len(bin) < 4:
        result['text'] = "0"
        return
    numero = 0
    potenza = int(len(bin)) -1
    for x in bin:
        if x == '0':
            pass
        else:
            numero += 2**potenza
        potenza -= 1
    result['text'] = numero

sv = StringVar()
sv.trace("w",lambda a,b,c: translate())
input = Entry(root, width=50,textvariable=sv)
input.focus()
input.pack(expand=True, ipady=5)
result =ttk.Label(root,text="0",font=("helvetica underline",30))
result.pack(expand=True)


root.mainloop()
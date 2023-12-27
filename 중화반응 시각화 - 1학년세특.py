from tkinter import *
from time import sleep
# NaOH + HCl => H2O + Na(+) + Cl(-)
window=Tk()
window.geometry("640x400")
canvas=Canvas(window,width=640,height=300,bg="aqua")
canvas.pack()
#NaOH
O=canvas.create_oval(200,150,150,100,fill="red")#산소
H1=canvas.create_oval(170,170,140,140,fill="blue")#수소
Na=canvas.create_oval(250,150,190,90,fill="purple")#나트륨
#HCl
H2=canvas.create_oval(370,170,340,140,fill="blue")#수소
Cl=canvas.create_oval(400,150,340,90,fill="green")#염소
def click():
  lbl["text"]="H(+) + Cl(-) + OH(-) + Na(+)"
  for i in range(31):
    canvas.move(H2,-5,0)
    canvas.move(Na,0,-2)
    window.update()
    sleep(0.2)
  lbl["text"]="H2O + Na(+) + Cl(-) (+ 열)"
lbl=Label(window,text="NaOH + HCl")
lbl.pack()
btn=Button(window,text="반응 진행",command=click)
btn.pack()
window.mainloop()

from tkinter import *
import math
root=Tk()
root.geometry("1000x750")
root.title("Graphing cuz i cant come up with better name")
canvas = Canvas(root, width=1000, height=1000)
canvas.pack()
dict={1:[2,6,4],2:[5],3:[1,5],7:[8,2,9]}
l1=[]
for i in dict:
    if(i not in l1):
        l1.append(i)
    for j in dict[i]:
        if j not in l1:
            l1.append(j)
print(l1)
for i in l1:
    c1=300+200*(math.cos(l1.index(i)*2*math.pi/len(l1)))
    c2=300+200*(math.sin(l1.index(i)*2*math.pi/len(l1)))
    canvas.create_oval(c1-10, c2-10, c1+10, c2+10, outline='black')
    canvas.create_text(c1,c2,text=i)
    if i in dict:
        for j in dict[i]:
            c3=300+200*(math.cos(l1.index(j)*2*math.pi/len(l1)))
            c4=300+200*(math.sin(l1.index(j)*2*math.pi/len(l1)))
            canvas.create_line(c1,c2,c3,c4)
root.mainloop()
from tkinter import *
root=Tk()
root.geometry("700x350")
root.title("Graphing cuz i cant come up with better name")
canvas = Canvas(root, width=200, height=200)
canvas.pack()
dict={1:[2,4],2:[5],3:[1,5]}
l1=[]
for i in dict:
    if(i not in l1):
        l1.append(i)
    for j in dict[i]:
        if j not in l1:
            l1.append(j)
print(l1)
for i in l1:
    if i%2!=0:
        x0, y0, x1, y1 = 10, 10+40*(i-1), 30, 30+40*(i-1)
    else:
        x0, y0, x1, y1 = 50, 10+40*(i-2), 70, 30+40*(i-2)
    canvas.create_oval(x0, y0, x1, y1, outline='black')
    canvas.create_text((x0+x1)/2,(y0+y1)/2,text=i)
    if i in dict:
        for j in dict[i]:
            if j % 2 != 0:
                x0, y0, x1, y1 = 10, 10 + 40 * (i - 1), 30, 30 + 40 * (i - 1)
            else:
                x0, y0, x1, y1 = 50, 10 + 40 * (i - 2), 70, 30 + 40 * (i - 2)
            canvas.create_line(10,10,70,30)
root.mainloop()
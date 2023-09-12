from tkinter import *
import math
root=Tk()
root.geometry("1000x750")
root.title("Graphing cuz i cant come up with better name")
canvas = Canvas(root, width=1000, height=1000)
canvas.pack()
dict={1:[2],2:[3],3:[4,5],4:[2],5:[6],6:[7],7:[8,12],8:[9,10],9:[7],10:[11],12:[9],13:[12,6]}
dict={1:[2],2:[3],3:[1,4],4:[2]}
l1=[]
dict2={}
'''in 3 sided , if its on base of third side its , the initial's triangle second side isnt red
    if on base of first side, the new triangle isnt red
    if on base of 2nd side, ITS WORKING FOR SOME STUPID REASON
'''
def closed_loop(i,j):
    global dict2
    c3 = 300 + 190 * (math.cos(l1.index(j) * 2 * math.pi / len(l1)))
    c4 = 300 + 190 * (math.sin(l1.index(j) * 2 * math.pi / len(l1)))
    c1 = 300 + 190 * (math.cos(l1.index(i) * 2 * math.pi / len(l1)))
    c2 = 300 + 190 * (math.sin(l1.index(i) * 2 * math.pi / len(l1)))
    color=["black","red"]
    s=0
    if f"{i}->{j}" not in dict2:
        dict2[f"{i}->{j}"] = "taken"
    elif dict2[f"{i}->{j}"] == "black":
        return 1
    elif dict2[f"{i}->{j}"] == "red":
        return 1
    elif dict2[f"{i}->{j}"] == "taken":
        canvas.create_line(c1, c2, c3, c4, arrow="last", fill="red")
        dict2[f"{i}->{j}"] = "red"
        return 2
    if(j in dict):
        if dict[j] == []:
            canvas.create_line(c1, c2, c3, c4, arrow="last", fill="black")
            dict2[f"{i}->{j}"] = color[s - 1]
            return 1
        for k in dict[j]:
            a=closed_loop(j,k)
            if(s!=2):
                s=a
    else:
            canvas.create_line(c1, c2, c3, c4, arrow="last", fill="black")
            dict2[f"{i}->{j}"] = color[s - 1]
            return 1

    if dict2[f"{i}->{j}"] != "red":
        canvas.create_line(c1, c2, c3, c4, arrow="last", fill=color[s-1])
        dict2[f"{i}->{j}"] = color[s-1]
    else:
        return 1
    return s
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

            if i==j:
                c1 = 300 + 220 * (math.cos(l1.index(i) * 2 * math.pi / len(l1)))
                c2 = 300 + 220 * (math.sin(l1.index(i) * 2 * math.pi / len(l1)))
                c3  = 300 + 210 * (math.cos(l1.index(i) * 2 * math.pi / len(l1)))
                c4 = 300 + 210 * (math.sin(l1.index(i) * 2 * math.pi / len(l1)))
                canvas.create_oval(c1 - 10, c2 - 10, c1 + 10, c2 + 10, outline='red',)
                canvas.create_line(c3,c4,300 + 210 * (math.cos(l1.index(i) * 2 * math.pi / len(l1)+0.03)),300 + 210 * (math.sin(l1.index(i) * 2 * math.pi / len(l1)+0.03)),arrow="last",fill="red")
            elif f"{i}->{j}" not in dict2:
                (closed_loop(i, j))
print(dict2)
root.mainloop()
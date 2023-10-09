from tkinter import *
import math
import copy
root = Tk()
root.geometry("1000x750")
root.title("Graphing cuz i cant come up with better name")
canvas = Canvas(root, width=1000, height=1000)
canvas.pack()
dict = {1: [2], 2: [3], 3: [4, 5], 4: [2], 5: [6], 6: [5,7], 7: [8, 12], 8: [9, 10], 9: [7], 10: [11], 12: [9,14],13:[5]}

sequence = []
SCC={}
def order(dict,i,passed,order_temp):
    if i not in passed:
        passed.append(i)
        if i not in dict or dict[i]==[]:
            order_temp.append(i)
            return
        else:
            for j in dict[i]:
                order(dict,j,passed,order_temp)
            order_temp.append(i)
    else:
        return

def dfs(dict,i,passed,SCC1):
    if i in passed:
        return
    passed.append(i)
    if i in dict:
        for j in dict[i]:
            dfs(dict,j,passed,SCC1)
    SCC1.append(i)
def reverse(dict):
    dict2={}
    for i in dict:
        for j in dict[i]:
            if j not in dict2:
                dict2[j]=[]
            dict2[j].append(i)
    return dict2
def kosaraju(dict,SCC,sequence):
    SCC2=[]
    order_temp=[]
    passed=[]
    SCC1=[]
    for i in dict:
        order(dict, i,passed,order_temp)
    passed=[]
    sequence.extend(order_temp)
    dict=reverse(dict)
    while order_temp!=[]:
        a=order_temp.pop()
        if a not in passed:
            dfs(dict,a,passed,SCC1)
            if SCC1!=[]:
                SCC2.append(SCC1)
            SCC1=[]
    sequence.sort()
    for i in sequence:
        for k in SCC2:
            if i in k :
                if [i]==k:
                    SCC[i]=[]
                else:
                    SCC[i] = k
def graphs(dict,SCC,sequence):
    for i in sequence:
        c1 = 300 + 200 * (math.cos(sequence.index(i) * 2 * math.pi / len(sequence)))
        c2 = 300 + 200 * (math.sin(sequence.index(i) * 2 * math.pi / len(sequence)))
        canvas.create_oval(c1 - 10, c2 - 10, c1 + 10, c2 + 10, outline='black')
        canvas.create_text(c1, c2, text=i)
        if i in dict:
            for j in dict[i]:
                if i == j:
                    c1 = 300 + 220 * (math.cos(sequence.index(i) * 2 * math.pi / len(sequence)))
                    c2 = 300 + 220 * (math.sin(sequence.index(i) * 2 * math.pi / len(sequence)))
                    c3 = 300 + 210 * (math.cos(sequence.index(i) * 2 * math.pi / len(sequence)))
                    c4 = 300 + 210 * (math.sin(sequence.index(i) * 2 * math.pi / len(sequence)))
                    canvas.create_oval(c1 - 10, c2 - 10, c1 + 10, c2 + 10, outline='red', )
                    canvas.create_line(c3, c4,
                                       300 + 210 * (math.cos(sequence.index(i) * 2 * math.pi / len(sequence) + 0.03)),
                                       300 + 210 * (math.sin(sequence.index(i) * 2 * math.pi / len(sequence) + 0.03)),
                                       arrow="last",
                                       fill="red")
                else:
                    c3 = 300 + 190 * (math.cos(sequence.index(j) * 2 * math.pi / len(sequence)))
                    c4 = 300 + 190 * (math.sin(sequence.index(j) * 2 * math.pi / len(sequence)))
                    c1 = 300 + 190 * (math.cos(sequence.index(i) * 2 * math.pi / len(sequence)))
                    c2 = 300 + 190 * (math.sin(sequence.index(i) * 2 * math.pi / len(sequence)))

                    if j in SCC[i]:
                        canvas.create_line(c1, c2, c3, c4, arrow="last", fill="red")
                    else:
                        canvas.create_line(c1, c2, c3, c4, arrow="last", fill="black")
def count_path(dict,SCC,i,b,ele,count,count_dict):
    if i in ele:
        return
    ele.append(i)
    count+=1
    if(i==b):
        if count in count_dict:
            count_dict[count].append(copy.copy(ele))
            ele.pop()
            return
        else:
            count_dict[count]=[copy.copy(ele)]
            ele.pop()
            return
    if i in dict:
        for j in dict[i]:
            count_path(dict,SCC,j,b,ele,count,count_dict)
    ele.pop()
    count-=1

def shortestpath(dict,SCC,a,b):
    count=0
    count_dict={}
    ele=[a]
    for i in dict[a]:
        count_path(dict,SCC,i,b,ele,count,count_dict)
        count=0
    if count_dict=={}:
        print(f"There is no path from {a} to {b}")
    else:
        print(f"shortest path from {a} to {b} is",count_dict[min(count_dict)])
kosaraju(dict,SCC,sequence)
graphs(dict,SCC,sequence)

a=int(input("enter a:"))
b=int(input("enter b:"))
shortestpath(dict,SCC,a,b)
root.mainloop()


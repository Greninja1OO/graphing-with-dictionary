from tkinter import *
import math
import copy

root = Tk()
root.geometry("1000x750")
root.title("Graphing cuz i cant come up with better name")
canvas = Canvas(root, width=1000, height=1000)
canvas.pack()
graph={}
# graph = {1: [2], 2: [3], 3: [4, 5], 4: [2], 5: [6], 6: [5, 7], 7: [8, 12], 8: [9, 10], 9: [7], 10: [11], 12: [9, 14],
#         13: [5]}

weight_edge={}
sequence = []
SCC = {}

def edges(graph,weight_edge):
    n=int(input("Enter number of edges "))
    for i in range(0,n):
        a,b=input("Enter the edge ").split()
        a=int(a)
        b=int(b)
        c=int(input("Enter the weight "))
        if a in graph:
            graph[a].append(b)
        else:
            graph[a]=[b]
        weight_edge[(a,b)]=c
def order(graph, i, passed, order_temp):
    if i not in passed:
        passed.append(i)
        if i not in graph or graph[i] == []:
            order_temp.append(i)
            return
        else:
            for j in graph[i]:
                order(graph, j, passed, order_temp)
            order_temp.append(i)
    else:
        return


def dfs(graph, i, passed, SCC1):
    if i in passed:
        return
    passed.append(i)
    if i in graph:
        for j in graph[i]:
            dfs(graph, j, passed, SCC1)
    SCC1.append(i)


def reverse(graph):
    graph2 = {}
    for i in graph:
        for j in graph[i]:
            if j not in graph2:
                graph2[j] = []
            graph2[j].append(i)
    return graph2


def kosaraju(graph, SCC, sequence):
    SCC2 = []
    order_temp = []
    passed = []
    SCC1 = []
    for i in graph:
        order(graph, i, passed, order_temp)
    passed = []
    sequence.extend(order_temp)
    graph = reverse(graph)
    while order_temp != []:
        a = order_temp.pop()
        if a not in passed:
            dfs(graph, a, passed, SCC1)
            if SCC1 != []:
                SCC2.append(SCC1)
            SCC1 = []
    sequence.sort()
    for i in sequence:
        for k in SCC2:
            if i in k:
                if [i] == k:
                    SCC[i] = []
                else:
                    SCC[i] = k


def graphs(graph, SCC, sequence):
    for i in sequence:
        c1 = 300 + 200 * (math.cos(sequence.index(i) * 2 * math.pi / len(sequence)))
        c2 = 300 + 200 * (math.sin(sequence.index(i) * 2 * math.pi / len(sequence)))
        canvas.create_oval(c1 - 10, c2 - 10, c1 + 10, c2 + 10, outline='black')
        canvas.create_text(c1, c2, text=i)
        if i in graph:
            for j in graph[i]:
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


def count_path(graph,weight_edge, SCC, i, b, ele, count, count_graph):
    if i in ele:
        return
    ele.append(i)
    if (i == b):
        if count in count_graph:
            count_graph[count].append(copy.copy(ele))
            ele.pop()
            return
        else:
            count_graph[count] = [copy.copy(ele)]
            ele.pop()
            return
    if i in graph:
        for j in graph[i]:
            count += weight_edge[(i,j)]
            count_path(graph,weight_edge, SCC, j, b, ele, count, count_graph)
            count-=weight_edge[(i,j)]
    ele.pop()



def shortestpath(graph,weight_edge, SCC, a, b):
    count_graph = {}
    ele = [a]
    for i in graph[a]:
        count=weight_edge[(a,i)]
        count_path(graph,weight_edge, SCC, i, b, ele, count, count_graph)
    if count_graph == {}:
        print(f"There is no path from {a} to {b}")
    else:
        print(f"shortest path from {a} to {b} is", count_graph[min(count_graph)])

edges(graph,weight_edge)
kosaraju(graph, SCC, sequence)
graphs(graph, SCC, sequence)

a = int(input("enter a:"))
b = int(input("enter b:"))
shortestpath(graph,weight_edge, SCC, a, b)
root.mainloop()

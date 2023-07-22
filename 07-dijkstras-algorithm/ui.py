from tkinter import *
from main import grid


PLATINUM = "#e7e7e7"

window = Tk()
window.title("Dijkstra's Algorithm")
window.config(padx=50, pady=50, bg=PLATINUM)

canvas = Canvas(width=200, height=200, bg=PLATINUM, highlightthickness=0)

for item in grid:
    Label(text=item+1, bg=PLATINUM).grid(row=grid[item][0], column=grid[item][1])



window.mainloop()
from tkinter import *
from constants import *
import utils
from cell import Cell

root = Tk()
root.configure(bg = 'black')
root.geometry(f'{WIDTH}x{HEIGHT}')
root.resizable(False, False)
root.title('Minesweeper game')

top_frame = Frame(root, bg= 'black', height= utils.height_percent(15), width= WIDTH)
top_frame.place(x=0, y=0)

label = Label(top_frame, bg= 'black', fg= 'white', text= 'Minesweeper Game', font= ('', 38))
label.place(x=utils.width_percent(30), y= 0)

left_frame = Frame(root, bg= 'black', height= utils.height_percent(75), width= utils.width_percent(25))
left_frame.place(x=0, y=utils.height_percent(15))

center_frame = Frame(root, bg= 'black', height= utils.height_percent(85), width= utils.width_percent(75))
center_frame.place(x=utils.width_percent(25), y=utils.height_percent(15))

for x in range(GRID_SIZE):
    for y in range(GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(column = x, row = y)

Cell.randomize_mines()

Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)

root.mainloop()
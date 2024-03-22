from constants import *
from tkinter import Button, Label
import random
import ctypes
import sys

class Cell:
    all = []
    cell_count = CELL_COUNT
    cell_count_label_object = None

    def __init__(self, x, y, is_mine=False) -> None:
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y

        Cell.all.append(self)
    
    def create_btn_object(self, location):
        btn = Button(location, width=10, height=3)
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)

        self.cell_btn_object = btn

    def left_click_actions(self, _):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_count == 0:
                for cell in self.surrounded_cells:
                    cell.show_cell()
            self.show_cell()

            if Cell.cell_count == CELL_COUNT- MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, 'Congratulations! You won the game.', 'Game Over', 0)

        
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')

    @staticmethod
    def create_cell_count_label(location):
        label = Label(location, fg='white', bg= 'black', font=('', 20), text=f'Cells Left: {Cell.cell_count-MINES_COUNT}')
        Cell.cell_count_label_object = label


    def is_valid_cell(self, x, y):

        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
            
        return None


    @property
    def surrounded_cells(self):
        cells = [self.is_valid_cell(self.x - 1, self.y - 1),
                 self.is_valid_cell(self.x - 1, self.y),
                 self.is_valid_cell(self.x - 1, self.y + 1),
                 self.is_valid_cell(self.x, self.y - 1),
                 self.is_valid_cell(self.x, self.y + 1),
                 self.is_valid_cell(self.x + 1, self.y - 1),
                 self.is_valid_cell(self.x + 1, self.y),
                 self.is_valid_cell(self.x + 1, self.y + 1)]
        
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_count(self):
        count = 0

        for cell in self.surrounded_cells:
            if cell.is_mine:
                count += 1

        return count
    
    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            Cell.cell_count_label_object.config(text=f'Cells Left: {Cell.cell_count}')
            self.cell_btn_object.config(text=self.surrounded_cells_mines_count)

            self.cell_btn_object.config(bg='SystemButtonFace')

        self.is_opened = True

    def show_mine(self):
        self.cell_btn_object.config(bg='red')
        ctypes.windll.user32.MessageBoxW(0, 'You clicked a mine.', 'Game Over', 0)
        sys.exit()


    def right_click_actions(self, _):
        if not self.is_mine_candidate:
            self.cell_btn_object.config(bg='orange')
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.config(bg='SystemButtonFace')
            self.is_mine_candidate = False

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, MINES_COUNT)

        for picked_cell in picked_cells:
            picked_cell.is_mine = True



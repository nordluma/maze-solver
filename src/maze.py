import time
import random
from typing import Union

from cell import Cell
from graphics import Window


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: float,
        cell_size_y: float,
        win: Union[Window, None] = None,
        seed: Union[int, None] = None,
    ) -> None:
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._cells = []
        self._win = win

        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    def _create_cells(self):
        for i in range(self.num_cols):
            column = []
            for j in range(self.num_rows):
                column.append(Cell(self._win))
            self._cells.append(column)

        # we cannot call `self._draw_cell` during the cell creation since the
        # matrix has not been created, we would get a out of bounds error
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i: int, j: int):
        if not self._win:
            return

        x1 = self._x1 + i * self.cell_size_x
        x2 = x1 + self.cell_size_x
        y1 = self._y1 + j * self.cell_size_y
        y2 = y1 + self.cell_size_x

        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if not self._win:
            return

        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        max_col = self.num_cols - 1
        max_row = self.num_rows - 1
        self._cells[max_col][max_row].has_bottom_wall = False
        self._draw_cell(max_col, max_row)

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True

        while True:
            next_idx_list = []
            if i > 0 and not self._cells[i - 1][j].visited:  # North
                next_idx_list.append((i - 1, j))
            if i < self.num_cols - 1 and self._cells[i + 1][j].visited:  # South
                next_idx_list.append((i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:  # West
                next_idx_list.append((i, j - 1))
            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:  # East
                next_idx_list.append((i, j + 1))

            if len(next_idx_list) == 0:  # no directions to go to
                self._draw_cell(i, j)
                return

            direction_idx = random.randrange(len(next_idx_list))
            ni, nj = next_idx_list[direction_idx]
            next_cell = self._cells[ni][nj]

            if ni == i + 1:
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False
            if ni == i - 1:
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False
            if nj == j + 1:
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            if nj == j - 1:
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False

            self._break_walls_r(ni, nj)

import time
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
        cell_size_x: int,
        cell_size_y: int,
        win: Union[Window, None] = None,
    ) -> None:
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._cells = []
        self._win = win

        self._create_cells()

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

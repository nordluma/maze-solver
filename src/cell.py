from typing import Union
from graphics import Line, Point, Window


class Cell:
    def __init__(self, win: Union[Window, None]) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def __repr__(self) -> str:
        return f"cell at x: {self._x1} - {self._x2} y: {self._y1} - {self._y2}"

    def draw(self, x1: int, y1: int, x2: int, y2: int):
        if not self._win:
            return

        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_left_wall:
            self._win.draw_line(Line(Point(x1, y1), Point(x1, y2)))
        else:
            self._win.draw_line(Line(Point(x1, y1), Point(x1, y2)), "white")

        if self.has_top_wall:
            self._win.draw_line(Line(Point(x1, y1), Point(x2, y1)))
        else:
            self._win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "white")

        if self.has_right_wall:
            self._win.draw_line(Line(Point(x2, y1), Point(x2, y2)))
        else:
            self._win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "white")

        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(x1, y2), Point(x2, y2)))
        else:
            self._win.draw_line(Line(Point(x1, y2), Point(x2, y2)), "white")

    def draw_move(self, to_cell, undo: bool = False):
        if not self._win:
            return

        if not self._x2 or not self._x1 or not self._y2 or not self._y1:
            return

        half_len = abs(self._x2 - self._x1) // 2
        x_center = half_len + self._x1
        y_center = half_len + self._y1

        half_len_2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center_2 = half_len_2 + to_cell._x1
        y_center_2 = half_len_2 + to_cell._y1

        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(Point(x_center, y_center), Point(x_center_2, y_center_2))
        self._win.draw_line(line, fill_color)

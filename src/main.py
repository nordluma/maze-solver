from cell import Cell
from graphics import Window


def main():
    win = Window(800, 600)

    cell = Cell(win)
    cell.has_left_wall = False
    cell.draw(50, 50, 100, 100)

    cell = Cell(win)
    cell.has_right_wall = False
    cell.draw(125, 125, 200, 200)

    cell = Cell(win)
    cell.has_bottom_wall = False
    cell.draw(225, 225, 250, 250)

    cell = Cell(win)
    cell.has_top_wall = False
    cell.draw(300, 300, 500, 500)

    win.wait_for_close()


if __name__ == "__main__":
    main()

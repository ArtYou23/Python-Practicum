class Checkers:

    def __init__(self):
        self.cells = dict()
        for row in '87654321':
            c = 0
            for col in 'ABCDEFGH':
                if c % 2 == 1 and (row == '6' or row == '8'):
                    self.cells[col + row] = Cell('B')
                elif c % 2 == 1 and (row == '2'):
                    self.cells[col + row] = Cell('W')
                elif c % 2 == 0 and (row == '7'):
                    self.cells[col + row] = Cell('B')
                elif c % 2 == 0 and (row == '3' or row == '1'):
                    self.cells[col + row] = Cell('W')
                else:
                    self.cells[col + row] = Cell('X')
                c += 1

    def get_cell(self, cell):
        return self.cells[cell]

    def move(self, where_from, where_to):
        check = self.cells[where_from].remove_check()
        return self.cells[where_to].set_check(check)


class Cell:

    def __init__(self, cell_item='X') -> None:
        self.condition = cell_item

    def status(self):
        return self.condition

    def remove_check(self):
        check = self.status()
        self.condition = 'X'
        return check

    def set_check(self, check):
        old_check = self.status()
        self.condition = check
        return old_check
import time

from mcpi.event import BlockEvent
from mcpi.minecraft import Minecraft


class Drawable:
    def __init__(self, mc: Minecraft, x: int, y: int, z: int):
        self.mc = mc
        self.x = x
        self.y = y
        self.z = z
        self.children: [Drawable] = []

    def draw(self):
        for i in range(len(self.children)):
            self.children[i].draw()

    def clean(self):
        self.mc.setBlock(self.x, self.y, self.z, 0)
        for i in range(len(self.children)):
            self.children[i].clean()

    def move(self, x, y, z):
        self.clean()
        self.x = x
        self.y = y
        self.z = z
        self.draw()


class BoardCell(Drawable):
    CONCRETE = 251
    WHITE_CELL_BLOCK = 0
    BLACK_CELL_BLOCK = 15
    BLUE_CELL_BLOCK = 3

    def __init__(self, mc, x, y, z, black: bool):
        super().__init__(mc, x, y, z)
        self.black = black
        self.highlighted = False

    def draw(self):
        if not self.highlighted:
            self.mc.setBlock(self.x, self.y, self.z, BoardCell.CONCRETE,
                             BoardCell.BLACK_CELL_BLOCK if self.black else BoardCell.WHITE_CELL_BLOCK)
        else:
            self.mc.setBlock(self.x, self.y, self.z, BoardCell.CONCRETE, BoardCell.BLUE_CELL_BLOCK)


class ChessBoard(Drawable):
    def __init__(self, mc, x, y, z):
        super().__init__(mc, x, y, z)
        self.cells = [[None] * 8 for i in range(8)]
        for x in range(len(self.cells)):
            row = self.cells[x]
            for z in range(len(row)):
                cell = BoardCell(self.mc, self.x + x, self.y, self.z + z,
                                 False if (x + z) % 2 == 0 else True)
                self.cells[x][z] = cell
                self.children.append(cell)

    def set_highlights(self, hl):
        for x in range(len(self.cells)):
            row = self.cells[x]
            for z in range(len(row)):
                row[z].highlighted = False
        for h in hl:
            self.cells[h[0]][h[1]].highlighted = True


class Checker(Drawable):
    def __init__(self, mc, x, y, z, black: bool):
        super().__init__(mc, x, y, z)
        self.black = black
        self.king = False
        self.killed = False

    def draw(self):
        block = None
        if self.killed:
            block = (0, 0)
        else:
            if self.black:
                block = (95, 15)
            else:
                block = (95, 0)
        self.mc.setBlock(self.x, self.y, self.z, block[0], block[1])
        if self.king:
            self.mc.setBlock(self.x, self.y + 1, self.z, block[0], block[1])


class Game(Drawable):
    def __init__(self, mc, x, y, z):
        super().__init__(mc, x, y, z)
        board = ChessBoard(self.mc, self.x, self.y, self.z)
        self.children.append(board)
        matrix = [[None] * 8 for i in range(8)]
        for row in range(8):
            team = 1 if (row < 3) else 2 if (row >= 5) else 0
            if team == 0:
                continue
            for col in range(8):
                black_cell = not ((row + col) % 2 == 0)
                if black_cell:
                    (x, y, z) = self.get_global_pos(col, row)
                    checker = Checker(self.mc, x, y + 1, z, team == 1)
                    matrix[col][row] = checker
                    self.children.append(checker)
        self.matrix: [[Checker]] = matrix
        self.board = board
        self.selected = {
            'checker': None,
            'x': None,
            'y': None,
            'possible': None
        }

    def get_global_pos(self, x: int, y: int):
        return self.x + x, self.y, self.z + y

    def get_board_pos(self, x: int, y: int, z: int):
        if (y - self.y) < 0 or (y - self.y) > 1:
            return None
        bx = x - self.x
        by = z - self.z
        if bx < 0 or bx >= 8 or by < 0 or by >= 8:
            return None
        return bx, by

    def click(self, x, y, z):
        board_pos = self.get_board_pos(x, y, z)
        print("board_pos", board_pos)
        if board_pos is not None:
            self.board.set_highlights([])
            (x, y) = board_pos
            checker = self.matrix[x][y]
            if checker is not None:
                possible_steps = self.get_possible_steps(x, y, checker.black)
                self.selected['x'] = x
                self.selected['y'] = y
                self.selected['checker'] = checker
                self.selected['possible'] = possible_steps
                print("possible_steps", possible_steps)
                self.board.set_highlights(possible_steps)
            else:
                if self.selected['checker'] is not None:
                    for pos in self.selected['possible']:
                        if pos[0] == x and pos[1] == y:
                            self.matrix[self.selected['x']][self.selected['y']] = None
                            self.matrix[x][y] = self.selected['checker']
                            (gx, gy, gz) = self.get_global_pos(x, y)
                            self.selected['checker'].move(gx, gy + 1, gz)
                            self.selected['checker'] = None
                            break
            self.draw()

    def get_possible_steps(self, x, y, black: bool, kills_only: bool = False):
        print("get_possible_steps", x, y, black)
        y_step = 1 if black else -1
        possible_steps = [(x - 1, y + y_step), (x + 1, y + y_step)]
        steps = []
        for i in range(len(possible_steps)):
            step = possible_steps[i]
            print("step", step)
            if not self.in_range(step[0], step[1]):
                continue
            checker = self.matrix[step[0]][step[1]]
            # Если стоит какая-то пешка
            if checker is not None:
                # Если стоит моя, то игнорим
                if checker.black == black:
                    continue
                # Если не моя, то ищем варианты побить
                (kx, ky) = (step[0] + step[0] - x, step[1] + y_step)
                if self.in_range(kx, ky) and self.matrix[kx][ky] is not None:
                    steps.append((kx, ky))
                    for kill_step in self.get_possible_steps(kx, ky, black, True):
                        steps.append(kill_step)
            elif not kills_only:
                steps.append(step)
        return steps

    def in_range(self, x, y):
        return 0 <= x < 8 and 0 <= y < 8


class MinecraftCheckers:
    def __init__(self):
        self.mc = Minecraft.create()
        self.pos = self.mc.player.getTilePos()
        self.game = Game(self.mc, self.pos.x, self.pos.y, self.pos.z)
        self.game.draw()

    def loop(self):
        while True:
            events = self.mc.events.pollBlockHits()
            for event in events:
                if event.type == BlockEvent.HIT:
                    self.game.click(event.pos.x, event.pos.y, event.pos.z)
            time.sleep(0.1)


checkers = MinecraftCheckers()
checkers.loop()

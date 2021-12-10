import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color('white'),
                                 (x * self.cell_size + self.left,
                                  y * self.cell_size + self.top,
                                  self.cell_size, self.cell_size), 1)

    def get_cell(self, mouse_pos):
        self.x = (mouse_pos[0] - self.left) // self.cell_size
        self.y = (mouse_pos[1] - self.top) // self.cell_size
        if self.top < mouse_pos[1] < self.top + self.cell_size * self.height:
            if self.left < mouse_pos[0] < self.left + self.cell_size * self.width:
                self.board[self.y][self.x] = 1
                return self.x, self.y
        return None

    def on_click(self, coords):
        print(coords)
        print(self.board)

    def get_clicked(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)
        self.draw_cell()

    def draw_cell(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[self.y][self.x] == 1:
                    pygame.draw.rect(screen, pygame.Color('white'),
                                    (self.x * self.cell_size + self.left,
                                    self.y * self.cell_size + self.top,
                                    self.cell_size, self.cell_size))
                    pygame.display.flip()
        print('asasas')

class Life(Board):
    def die_or_alive(self):
        for i in range(len(self.board)):
            for j in range(len(board)):
                pass




if __name__ == '__main__':
    pygame.init()
    size = width, height = 620, 620
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color('black'))
    board = Life(30, 30)
    board.set_view(10, 10, 20)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                board.get_clicked(event.pos)
            board.render(screen)
            pygame.display.flip()

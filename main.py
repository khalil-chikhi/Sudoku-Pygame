import pygame
import random
import numpy as np
grids = []
lists = [
    '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......',
    '52...6.........7.13...........4..8..6......5...........418.........3..2...87.....',
    '6.....8.3.4.7.................5.4.7.3..2.....1.6.......2.....5.....8.6......1....',
    '48.3............71.2.......7.5....6....2..8.............1.76...3.....4......5....',
    '....14....3....2...7..........9...3.6.1.............8.2.....1.4....5.6.....7.8...',
    '......52..8.4......3...9...5.1...6..2..7........3.....6...1..........7.4.......3.',
    '6.2.5.........3.4..........43...8....1....2........7..5..27...........81...6.....',
    '.524.........7.1..............8.2...3.....6...9.5.....1.6.3...........897........',
    '6.2.5.........4.3..........43...8....1....2........7..5..27...........81...6.....',
    '.923.........8.1...........1.7.4...........658.........6.5.2...4.....7.....9.....',
    '6..3.2....5.....1..........7.26............543.........8.15........4.2........7..',
    '.6.5.1.9.1...9..539....7....4.8...7.......5.8.817.5.3.....5.2............76..8...',
    '3.6.7...........518.........1.4.5...7.....6.....2......2.....4.....8.3.....5.....'
]
for element in lists:

    newlist = list(map(lambda x: x.replace('.', '0'), element))
    newlist2 = list(map(int, newlist))
    chunk = np.array_split(newlist2, 9)
    chunk2 = np.array(chunk)
    chunk2.reshape(9, 9)
    grids.append(chunk2)

grid = random.choice(grids)

WIDTH = 550
original_value_color = (251, 31, 151)
background_color = (251, 247, 245)
buffer = 5

grid_original = [[grid[x][y]
                  for y in range(len(grid[0]))] for x in range(len(grid))]


def insert(win, position):
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    i, j = position[1], position[0]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if (grid_original[i-1][j-1] != 0):
                    return
                if (event.key == 48):
                    grid[i-1][j-1] = event.key-48
                    pygame.draw.rect(
                        win, background_color, (position[0]*50 + buffer, position[1]*50+buffer, 50-2*buffer, 50-2*buffer))
                    pygame.display.update()
                if (0 < event.key-48 < 10):
                    pygame.draw.rect(
                        win, background_color, (position[0]*50 + buffer, position[1]*50+buffer, 50-2*buffer, 50-2*buffer))
                    value = myfont.render(str(event.key-48), True, (0, 0, 0))
                    win.blit(value, (position[0]*50+15, position[1]*50))
                    grid[i-1][j-1] = event.key - 48
                    pygame.display.update()
                    return
                return


def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("SUDOKU")
    win.fill(background_color)
    myfont = pygame.font.SysFont('Comic Sans MS', 35)

    for i in range(0, 10):
        if (i % 3 == 0):
            pygame.draw.line(win, (0, 0, 0), (50 + 50*i, 50),
                             (50 + 50*i, 500), 4)
            pygame.draw.line(win, (0, 0, 0), (50, 50 + 50*i),
                             (500, 50 + 50*i), 4)

        pygame.draw.line(win, (0, 0, 0), (50 + 50*i, 50), (50 + 50*i, 500), 2)
        pygame.draw.line(win, (0, 0, 0), (50, 50 + 50*i), (500, 50 + 50*i), 2)
    pygame.display.update()

    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if (0 < grid[i][j] < 10):
                value = myfont.render(
                    str(grid[i][j]), True, original_value_color)
                win.blit(value, ((j+1)*50 + 15, (i+1)*50))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(win, (pos[0]//50, pos[1]//50))
            if event.type == pygame.QUIT:
                pygame.quit()


main()

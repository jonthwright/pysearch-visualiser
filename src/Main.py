import pygame
from Colour import colour
from Window import *

from algorithms.DFS import dfs
from algorithms.BFS import bfs
from algorithms.Astar import astar

WIDTH = 1000
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")


def main(win, width):
	print('\033c', end='')
	print('''
CONTROLS...
          
RIGHT MOUSE (CLICK): Set the start node (ORANGE), Set the target node (TURQOUISE).
RIGHT MOUSE (CLICK/DRAG): Draw the barrier nodes (BLACK) (Optional). Also clears any previous completed searches.
PRESS A-KEY: Select A-Star algorithm.
PRESS D-KEY: Select Depth First Search (DFS) algorithm.
PRESS B-KEY: Select Breath First Search (BFS) algorithm.
PRESS SPACEBAR: Start search (must have start and target node placed and search algorithm selected first)
PRESS BACKSPACE-KEY: Stop searching (only when searching starts). Also, clears anything all search results.


OTHER CONTROLS...

PRESS C-KEY: Clears screen entirely. Only when program is not searching.
PRESS ESC-KEY: Exit the app.
''')
	ROWS = 50
	grid = make_grid(ROWS, width)

	start = None
	end = None
	algorithm = None

	while True:
		draw(win, grid, ROWS, width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return pygame.quit()

			if pygame.mouse.get_pressed()[0]: # LEFT
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				node = grid[row][col]
				if not start and node != end:
					start = node
					start.make_start()

				elif not end and node != start:
					end = node
					end.make_end()

				elif node != end and node != start:
					clear_processing(grid)
					node.make_barrier()

			elif pygame.mouse.get_pressed()[2]: # RIGHT
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				node = grid[row][col]
				node.reset()

				if node == start:
					start = None
				elif node == end:
					end = None

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_b:
					algorithm = bfs
				if event.key == pygame.K_d:
					algorithm = dfs
				if event.key == pygame.K_a:
					algorithm = astar
				if event.key == pygame.K_c:
					start, end = None, None
					clear_screen(grid)
				if event.key == pygame.K_ESCAPE:
					return pygame.quit()
		
				if event.key == pygame.K_SPACE and start and end and algorithm:

					clear_processing(grid)

					for row in grid:
						for node in row:
							node.update_neighbours(grid)

					algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)

				if event.key == pygame.K_c:
					start = None
					end = None
					grid = make_grid(ROWS, width)


main(WIN, WIDTH)
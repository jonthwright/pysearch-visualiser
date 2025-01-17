import pygame
from Window import clear_processing
from Colour import colour

def reconstruct_path(cur_node, start, draw):
	while cur_node.previous and cur_node.previous != start:
		cur_node = cur_node.previous
		cur_node.make_path()
	draw()

def bfs(draw, grid, start, end):
	queue = [start]
	visited = set()

	while queue:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_BACKSPACE:
					clear_processing(grid)
					return False

		cur_node = queue.pop(0)

		if cur_node == end:
			reconstruct_path(cur_node, start, draw)
			end.make_end()
			return True

		if cur_node not in visited :
			visited.add(cur_node)
			for neighbour in cur_node.neighbours:				
				if neighbour.colour != colour.RED:
					queue.append(neighbour)
					neighbour.make_open()
					neighbour.previous = cur_node

		draw()

		if cur_node != start:
			cur_node.make_closed()

	return False
import pygame
import math
from queue import PriorityQueue
from Window_Func import clear_processing

def h(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return abs(x1 - x2) + abs(y1 - y2)


def reconstruct_path(cur_node, start, draw):
	while cur_node.previous and cur_node.previous != start:
		cur_node = cur_node.previous
		cur_node.make_path()
	draw()


def astar(draw, grid, start, end):
	count = 0
	open_set = PriorityQueue()
	open_set.put((0, count, start))
	g_score = {node: float("inf") for row in grid for node in row}
	g_score[start] = 0
	f_score = {node: float("inf") for row in grid for node in row}
	f_score[start] = h(start.get_pos(), end.get_pos())

	open_set_hash = {start}

	while not open_set.empty():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					clear_processing(grid)
					return False

		current = open_set.get()[2]
		open_set_hash.remove(current)

		if current == end:
			reconstruct_path(current, start, draw)
			end.make_end()
			return True

		for neighbour in current.neighbours:
			temp_g_score = g_score[current] + 1

			if temp_g_score < g_score[neighbour]:
				neighbour.previous = current
				g_score[neighbour] = temp_g_score
				f_score[neighbour] = temp_g_score + h(neighbour.get_pos(), end.get_pos())
				if neighbour not in open_set_hash:
					count += 1
					open_set.put((f_score[neighbour], count, neighbour))
					open_set_hash.add(neighbour)
					neighbour.make_open()

		draw()

		if current != start:
			current.make_closed()

	return False

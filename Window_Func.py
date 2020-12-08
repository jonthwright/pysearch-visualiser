import pygame
import math
from queue import PriorityQueue
from Colour import colour
from Node import Node

def clear_processing(grid):
	for row in grid:
		for node in row:
			if node.colour in {colour.RED, colour.PURPLE, colour.GREEN}:
				node.reset()

def make_grid(rows, width):
	grid = []
	gap = width // rows
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			node = Node(i, j, gap, rows)
			grid[i].append(node)

	return grid


def draw_grid(win, rows, width):
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win, colour.GREY, (0, i * gap), (width, i * gap))
		for j in range(rows):
			pygame.draw.line(win, colour.GREY, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width):
	win.fill(colour.WHITE)

	for row in grid:
		for node in row:
			node.draw(win)

	draw_grid(win, rows, width)
	pygame.display.update()


def get_clicked_pos(pos, rows, width):
	gap = width // rows
	y, x = pos

	row = y // gap
	col = x // gap

	return row, col

from Colour import colour
import pygame


class Node:
	def __init__(self, row, col, width, total_rows):
		self.row = row
		self.col = col
		self.x = row * width
		self.y = col * width
		self.colour = colour.WHITE
		self.neighbours = []
		self.width = width
		self.total_rows = total_rows
		self.previous = None
		self.dist = 0

	def get_pos(self):
		return self.row, self.col

	def is_closed(self):
		return self.colour == colour.RED

	def is_open(self):
		return self.colour == colour.GREEN

	def is_barrier(self):
		return self.colour == colour.BLACK

	def is_start(self):
		return self.colour == colour.ORANGE

	def is_end(self):
		return self.colour == colour.TURQUOISE

	def reset(self):
		self.colour = colour.WHITE

	def make_start(self):
		self.colour = colour.ORANGE

	def make_closed(self):
		if not self.is_start() and not self.is_end():
			self.colour = colour.RED

	def make_open(self):
		if self.colour not in {colour.ORANGE, colour.RED, colour.TURQUOISE}:
			self.colour = colour.GREEN

	def make_barrier(self):
		self.colour = colour.BLACK

	def make_end(self):
		self.colour = colour.TURQUOISE

	def make_path(self):
		self.colour = colour.PURPLE

	def draw(self, win):
		pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.width))

	def update_neighbours(self, grid):
		self.neighbours = []

		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN
			self.neighbours.append(grid[self.row + 1][self.col])

		if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
			self.neighbours.append(grid[self.row - 1][self.col])

		if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
			self.neighbours.append(grid[self.row][self.col + 1])

		if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
			self.neighbours.append(grid[self.row][self.col - 1])

	def __lt__(self, other):
		return False
	
	def __repr__(self):
		return f'Node(Row:{self.row}, Col:{self.col})'

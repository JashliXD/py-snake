import pygame as py
import random as ran
import time

py.init()
SIZE = 600
win = py.display.set_mode((SIZE,SIZE))
py.display.set_caption("Slithering Snake")

WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (100,100,100)

HEAD = (0,255,0)
TAIL = (65,198,65)

FOOD = (153,76,0)

class Spot:
	def __init__(self,row,col,SIZE, total_rows):
		self.row = row
		self.col = col
		self.x = row * SIZE
		self.y = col * SIZE
		self.total_rows = total_rows
		self.SIZE = SIZE
		self.color = WHITE
		self.adjacent = {"UP":[None,None],"DOWN":[None,None],"LEFT":[None,None],"RIGHT":[None,None]}

	def get_pos(self):
		return self.row,self.col

	def block(self):
		return self.color == BLACK

	def tail(self):
		return self.color == TAIL

	def open(self):
		return self.color == WHITE
	def food(self):
		return self.color == FOOD

	def head(self):
		return self.color == HEAD

	def make_food(self):
		self.color = FOOD

	def make_tail(self):
		self.color = TAIL

	def make_open(self):
		self.color = WHITE

	def make_head(self):
		self.color = HEAD

	def reset(self):
		self.color = WHITE

	def make_block(self):
		self.color = BLACK

	def draw(self,win):
		py.draw.rect(win,self.color,(self.x,self.y,self.SIZE, self.SIZE))

	def front(self,grid):
		
		#UP
		if grid[self.row][self.col-1].block() and control == 'UP':
			self.adjacent["UP"] = [self.row,self.col-1]
		#DOWN
		if grid[self.row][self.col+1].block() and control == 'DOWN':
			self.adjacent["DOWN"] = [self.row,self.col+1]
		#LEFT
		if grid[self.row-1][self.col].block() and control == 'LEFT':
			self.adjacent["LEFT"] = [self.row-1,self.col]
		#RIGHT
		if grid[self.row+1][self.col].block() and control == 'RIGHT':
			self.adjacent["RIGHT"] = [self.row+1,self.col]

		#UP
		if grid[self.row][self.col-1].open():
			self.adjacent["UP"] = [None,None]
		#DOWN
		if grid[self.row][self.col+1].open():
			self.adjacent["DOWN"] = [None,None]
		#LEFT
		if grid[self.row-1][self.col].open():
			self.adjacent["LEFT"] = [None,None]
		#RIGHT
		if grid[self.row+1][self.col].open():
			self.adjacent["RIGHT"] = [None,None]

def isNegative(num):
	if num < 0 and not num == 0:
		return True
	else:
		return False

def generatebox (rows ,width):
	grid = []
	gap =  width // rows
	for x in range(rows):
		grid.append([])
		for y in range(rows):
			spot = Spot(x,y,gap,rows)
			grid[x].append(spot)

	return grid

def drawBox(win,rows,width):
	gap = width // rows
	for x in range(rows):
		py.draw.line(win, GREY, (0, x * gap), (width, x * gap))
		for y in range(rows):
			py.draw.line(win, GREY, (y * gap, 0), (y * gap, width))

def draw(win,grid,rows,width):
	win.fill(WHITE)

	for row in grid:
		for spot in row:
			spot.draw(win)

	drawBox(win, rows,width)
	py.display.update()

def border():
	for e in range(ROWS):
		row,col = e,0
		spot = grids[e][0]
		spot2 = grids[0][e]
		spot3 = grids[ROWS-1][e]
		spot4 = grids[e][ROWS-1]

		spot.make_block()
		spot2.make_block()
		spot3.make_block()
		spot4.make_block()

def pos():
	col = ran.randint(2,47)
	row = ran.randint(2,47)
	return row,col

def deathborder():
	for i in range(ROWS):
		spot,spot2,spot3,spot4 = grids[i][0],grids[0][i],grids[ROWS-1][i],grids[i][ROWS-1]
		if spot == snake:
			game_over()
			run = False
		if spot2 == snake:
			game_over()
			run = False
		if spot3 == snake:
			game_over()
			run = False
		if spot4 == snake:
			game_over()
			run = False



# COPY PASTED CUZ LAZY
def game_over():
	win.fill(BLACK)
    # creating font object my_font
	gameover = py.font.SysFont('times new roman', 50)

	scoreText = py.font.SysFont('times new roman', 25)
	counterText = py.font.SysFont('times new roman', 25)
     
	# creating a text surface on which text
	# will be drawn
	game_over_surface = gameover.render(
		'GAME OVER', True, (255,0,0))

	score_surface = scoreText.render(
		'Score: '+str(score), True, (255,0,0))
	counter_surface = scoreText.render(
		'Food eaten: '+str(length), True, (255,0,0))
     
    # create a rectangular object for the text
    # surface object
	game_over_rect = game_over_surface.get_rect()
     
    # setting position of the text
	game_over_rect.midtop = (SIZE/2, SIZE/4)

    # blit wil draw the text on screen
	win.blit(game_over_surface, game_over_rect)
	win.blit(score_surface, (SIZE/2,SIZE/2))
	win.blit(counter_surface,(SIZE/2,(SIZE/2)+50))
	py.display.flip()
     
    # after 2 seconds we will quit the program
	time.sleep(3)
     
    # deactivating pygame library
	py.quit()
     
    # quit the program
	quit()


# print("GOING UP")
# print("GOING DOWN")
# print("GOING LEFT")
# print("GOING RIGHT")


def computer(control):
	row = snake.row
	col = snake.col
	if row == 1 and col == 1:
		if control == 'UP':
			control = "RIGHT"
			return control
		else:
			control = "DOWN"
			return control
	if row == 48 and col == 1: # EDITED NOT CHECKED
		if control == "UP":
			control = "LEFT"
			return control
		else:
			control = "DOWN"
			return control

	if row == 1 and col == 48: # CHECKED
		if control == "DOWN":
			control = "RIGHT"
			return control
		else:
			control = "UP"
			return control

	if row == 48 and col == 48: # CHECKED
		if control == 'DOWN':
			control = "LEFT"
			return control
		else:
			control = "UP"
			return control

	
	if snake.adjacent["UP"] != [None,None]:
		n = ran.randint(0,1)
		print('ADJACENT UP')
		if n == 1 and control != "LEFT":
			control = 'RIGHT'
			print("GOING RIGHT 1 ")
			return control
		else:
			control = 'LEFT'
			print("GOING LEFT 1")
			return control
	if snake.adjacent["DOWN"] != [None,None]:
		n = ran.randint(0,1)
		if n == 1 and control != "RIGHT":
			control = 'LEFT'
			print("GOING LEFT 2")
			return control
		if n == 0 and control != "LEFT":
			control = 'RIGHT'
			print("GOING RIGHT 2")
			return control
	if snake.adjacent["LEFT"] != [None,None]:
		n = ran.randint(0,1)
		print('ADJACENT LEFT')
		if n == 1 and control != "DOWN":
			control = 'UP'
			print("GOING UP 3")
			return control
		if n == 0 and control != "UP":
			control = 'DOWN'
			print("GOING DOWN 3")
			return control
	if snake.adjacent["RIGHT"] != [None,None]:
		n = ran.randint(0,1)
		print('ADJACENT RIGHT')
		if n == 1 and control != "UP":
			control = 'DOWN'
			print("GOING DOWN 4 ")
			return control
		if n == 0 and control != "DOWN":
			control = 'UP'
			print("GOING UP 4")
			return control

	if snake.row == foods.row:
		calculation = foods.col - snake.col
		print("FOOD FOUND IN ROW:"+str(row)+ " COL: "+str(calculation))
		if not isNegative(calculation) and control != "UP":
			control = 'DOWN'
			return control
		else:
			control = 'UP'
			return control

	if snake.col == foods.col:
		calculation = foods.row - snake.row
		print("FOOD FOUND IN ROW:"+str(calculation)+ " COL: "+str(col))
		if not isNegative(calculation) and control != "LEFT":
			control = 'RIGHT'
			return control
		else:
			control = 'LEFT'
			return control

	if snake.row == foods2.row:
		calculation = foods2.col - snake.col
		print("FOOD FOUND IN ROW:"+str(row)+ " COL: "+str(calculation))
		if not isNegative(calculation) and control != "UP":
			control = 'DOWN'
			return control
		else:
			control = 'UP'
			return control

	if snake.col == foods2.col:
		calculation = foods2.row - snake.row
		print("FOOD FOUND IN ROW:"+str(calculation)+ " COL: "+str(col))
		if not isNegative(calculation) and control != "LEFT":
			control = 'RIGHT'
			return control
		else:
			control = 'LEFT'
			return control

	return control


def snakemove(grid, snake_list,snake):
	gap = SIZE // ROWS
	for i in snake_list:

		row = i[0]
		col = i[1]
		spot = grids[row][col]
		x,y = spot.x,spot.y
		if spot == snake:
			py.draw.rect(win,HEAD,(x,y,gap,gap))
		else:
			py.draw.rect(win,TAIL,(x,y,gap,gap))

fps = py.time.Clock()
run = True

ROWS = 50
grids = generatebox(ROWS,SIZE)

snake=None
foods=None
foods2=None

score = 0

yspeed = 0
xspeed = 0

control = None

snake_list = []
length = 0
snake_speed= 15
while run:
	draw(win,grids,ROWS,SIZE)
	border()
	# BORDER
	if not snake:
		n = ran.randint(0,3)
		if n == 1:
			control = 'LEFT'
		elif n == 2:
			control = 'RIGHT'
		elif n == 3:
			control = 'DOWN'
		else:
			control = 'UP'
		row,col = pos()
		spot = grids[row][col]
		snake = spot
	if not foods:
		row,col = pos()
		spot = grids[row][col]
		foods = spot
		foods.make_food()
	if not foods2:
		row,col = pos()
		spot = grids[row][col]
		foods2 = spot
		foods2.make_food()
	# MAIN LOOP
	for event in py.event.get():
		if event.type == py.QUIT:
			run = False

	if snake != None:
		if control == 'UP':
			xspeed = 0
			yspeed = -1
		if control == 'DOWN':
			xspeed = 0
			yspeed = 1
		if control == 'LEFT':
			yspeed = 0
			xspeed = -1
		if control == 'RIGHT':
			yspeed = 0
			xspeed = 1
		snake.reset()
		if snake == foods:
			foods = None
			length += 1
			score += 10
		elif snake == foods2:
			foods2 = None
			length += 1
			score += 10
		row = snake.row + xspeed
		col = snake.col + yspeed
		spot = grids[row][col]
		snake = spot

		snake_head = []
		snake_head.append(snake.row)
		snake_head.append(snake.col)

		snake_list.append(snake_head)
		if len(snake_list) > length:
			del snake_list[0]

		snake.front(grids)
		for x in snake_list[:-1]:
			if x == snake_head:
				foods = None
				foods2 = None
				snake = None
				length = 0
				snake_list = []
				grids = generatebox(ROWS,SIZE)
		snakemove(grids, snake_list,snake)
		#snake.front(grids)
		if not snake:
			n = ran.randint(0,3)
			if n == 1:
				control = 'LEFT'
			elif n == 2:
				control = 'RIGHT'
			elif n == 3:
				control = 'DOWN'
			else:
				control = 'UP'
			row,col = pos()
			spot = grids[row][col]
			snake = spot
		if not foods:
			row,col = pos()
			spot = grids[row][col]
			foods = spot
			foods.make_food()
		if not foods2:
			row,col = pos()
			spot = grids[row][col]
			foods2 = spot
			foods2.make_food()
		control = computer(control)
		deathborder()
		py.display.update()
		snake.make_head()
		fps.tick(snake_speed)
import pygame
import pygame.math
import random


white = (255, 255, 255)
colour_dictionary1 = {
  2 : (217, 237, 146),
  4 : (181, 228, 140),
  8 : (153, 217, 140),
  16 : (118, 200, 147),
  32 : (82, 182, 154),
  64 : (52, 160, 164),
  128 : (22, 138, 173),
  256 : (26, 117, 159),
  512 : (30, 96, 145),
  1024 : (24, 78, 119),
  2048 : (252, 186, 3)
}
colour_dictionary2 = {
  2 : (76, 201, 240),
  4 : (72, 149, 239),
  8 : (67, 97, 238),
  16 : (63, 55, 201),
  32 : (58, 12, 163),
  64 : (72, 12, 168),
  128 : (86, 11, 173),
  256 : (114, 9, 183),
  512 : (181, 23, 158),
  1024 : (247, 37, 133),
  2048 : (252, 186, 3)
}
class Block:
    def __init__(self, value, x, y, size):
        self.value = value
        self.x = x
        self.y = y
        self.size = size


    def draw(self, theme):
        pygame.draw.rect(screen, (theme[self.value]), (self.x, self.y, self.size, self.size))
        font = pygame.font.SysFont('Arial', 25)
        text = font.render(str(self.value), 1, white)
        screen.blit(text, (self.x + self.size/2 - text.get_width()/2, self.y + int(self.size/2) - int(25/2)))


class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-4,self.y-4,self.width+8,self.height+8),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('Arial', 25)
            text = font.render(self.text, 1, white)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False


board = []
board_size = 4
for i in range(board_size):
    row = []
    for j in range(board_size):
        row.append(0)
    board.append(row)
pygame.init()
screen_size = (480, 480)
board_size = 440
screen = pygame.display.set_mode(screen_size)
is_running = True


def spawn_block():
    global board
    block_value = random.randint(1, 2) * 2
    while True:
        y = random.randint(0, 3)
        x = random.randint(0, 3)
        if board[y][x].value == 0:
            board[y][x].value = block_value
            break


def move_up():
    moved = False
    for y in range(1, 4):
      for x in range(4):
        if board[y][x].value != 0:
          for space in range(y):
            if board[space][x].value == 0:
              moved = True
              board[space][x].value = board[y][x].value
              board[y][x].value = 0
    for y in range(1, 4):
      for x in range(4):
        if board[y][x].value != 0:
          if board[y - 1][x].value == board[y][x].value:
            moved = True
            board[y - 1][x].value = (board[y][x].value * 2)
            board[y][x].value = 0
            for space in range(y, 3):
              board[space][x].value = board[space + 1][x].value
            board[3][x].value = 0
    return moved


def move_right():
    moved = False
    for y in range(2, -1, -1):
      for x in range(4):
        if board[x][y].value != 0:        
          for space in range(3, y, -1):
            if board[x][space].value == 0:
              moved = True
              board[x][space].value = board[x][y].value
              board[x][y].value = 0
    for y in range(2, -1, -1):
      for x in range(4):
        if board[x][y].value != 0:
          if board[x][y + 1].value == board[x][y].value:
            moved = True
            board[x][y + 1].value = (board[x][y].value * 2)
            board[x][y].value = 0
            for space in range(y, -1, -1):
              board[x][space].value = board[x][space - 1].value
            board[x][0].value = 0            
    return moved


def move_down():
    moved = False
    for y in range(2, -1, -1):
      for x in range(4):
        if board[y][x].value != 0:
          for space in range(3, y, -1):
            if board[space][x].value == 0:
              moved = True
              board[space][x].value = board[y][x].value
              board[y][x].value = 0
    for y in range(2, -1, -1):
      for x in range(4):
        if board[y][x].value != 0:
          if board[y + 1][x].value == board[y][x].value:
            moved = True
            board[y + 1][x].value = (board[y][x].value * 2)
            board[y][x].value = 0
            for space in range(y, -1, -1):
              board[space][x].value = board[space - 1][x].value
            board[0][x].value = 0
    return moved


def move_left():
    moved = False
    for y in range(1, 4):
      for x in range(4):
        if board[x][y].value != 0:
          for space in range(y):
            if board[x][space].value == 0:
              moved = True
              board[x][space].value = board[x][y].value
              board[x][y].value = 0
    for y in range(1, 4):
      for x in range(4):
        if board[x][y].value != 0:
          if board[x][y - 1].value == board[x][y].value:
            moved = True
            board[x][y - 1].value = (board[x][y].value * 2)
            board[x][y].value = 0
            for space in range(y, 3):
              board[x][space].value = board[x][space + 1].value
            board[x][3].value = 0
    return moved


for i in range(4):
    for j in range(4):
        board[i][j] = (Block(0, int(10 + (board_size/4)*(j+1)) - 95, int(10 + (board_size/4)*(i+1) - 95), 100))


spawn_block()
theme_chosen = False
theme = None
lost = False
while is_running:
    if not lost:
      button1 = button((153, 217, 140), 80, 100, 320, 120, "Emerald & Lapis Theme")
      button2 = button((67, 97, 238), 80, 250, 320, 120, "Sapphire & Ruby Theme")
      can_move = True
      filled = True
      screen.fill((white))
  
  # Choose theme screen
    
      if not theme_chosen:
        button1.draw(screen, (30, 96, 145))
        button2.draw(screen, (181, 23, 158))
        for event in pygame.event.get():
          mouse_pos = pygame.mouse.get_pos()
          
          if event.type == pygame.MOUSEBUTTONDOWN:
            if button1.isOver(mouse_pos):
              theme = colour_dictionary1
              theme_chosen = True
            elif button2.isOver(mouse_pos):
              theme = colour_dictionary2
              theme_chosen = True
            
          if event.type == pygame.MOUSEMOTION:
            if button1.isOver(mouse_pos):
              button1.color = (255, 0, 0)
            else:
              button1.color = (0, 255, 0)
  
  # Main Game
    
      else:
        for row in board:
            for block in row:
                if block.value > 0:
                    block.draw(theme)
                else:
                    filled = False
        if filled:
          can_move = False
          for y in range(3):
            if board[y][3].value == board[y + 1][3].value:
              can_move = True
            elif board[3][y].value == board[3][y + 1].value:
              can_move = True
            for x in range(3):
              value = board[y][x].value
              if board[y + 1][x].value == value or board[y][x + 1].value == value:
                can_move = True
          if not can_move:
            lost = True
    
    # GET EVENT 
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if can_move:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if move_up() == True:
                          spawn_block()
                    elif event.key == pygame.K_RIGHT:
                        if move_right() == True:
                          spawn_block()
                    elif event.key == pygame.K_DOWN:
                        if move_down() == True:
                          spawn_block()
                    elif event.key == pygame.K_LEFT:
                        if move_left() == True:
                          spawn_block()
    else:
      font = pygame.font.SysFont('Arial', 50)
      text = font.render("YOU LOST BOZO", 1, (255, 0, 0))
      screen.blit(text, (40, 200))


    pygame.display.flip()


pygame.quit()

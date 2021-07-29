from utils import *

# define window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Clone")

def init_grid(rows, cols, colour):
    grid = []
    
    for i in range(rows):
        grid.append([])
        for _ in range(cols): #variable not needed
            grid[i].append(colour)
    
    return grid

def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(win, BLACK, (0, i * PIXEL_SIZE), (WIDTH, i * PIXEL_SIZE))

        for i in range(COLS + 1):
            pygame.draw.line(win, BLACK, (i * PIXEL_SIZE, 0), (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))
            

def draw(win, grid, buttons):
    win.fill(BG_COLOUR)
    draw_grid(win, grid)

    for button in buttons:
        button.draw(win)
    pygame.display.update()

def get_row_col_from_pos(pos):
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    # prevents drawing in toolbar
    if row >= ROWS:
        raise IndexError

    return row, col

def flood_fill(win, target_colour):
    # start node from second click?
    # target colour -- colour of the cell -- second click?
    # replacement colour -- first click?
    replacement_colour = BLUE
    start_node = None
    


# event loop runs until game ends
running = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOUR)
drawing_colour = BLACK

first_row_button_y = HEIGHT - TOOLBAR_HEIGHT / 2 - 25 # y = 525
second_row_button_y = HEIGHT - TOOLBAR_HEIGHT / 2 + 10 # y = 560

buttons = [
    Button(10, first_row_button_y, 25, 25, BLACK),
    Button(45, first_row_button_y, 25, 25, RED),
    Button(80, first_row_button_y, 25, 25, GREEN),
    Button(115, first_row_button_y, 25, 25, BLUE),
    Button(150, first_row_button_y, 25, 25, YELLOW),
    Button(185, first_row_button_y, 25, 25, PINK),
    Button(225, first_row_button_y, 25, 25, WHITE, "E", BLACK),
    Button(260, first_row_button_y, 25, 25, WHITE, "C", BLACK),
    Button(225, second_row_button_y, 25, 25, WHITE, "T", BLACK),
    Button(260, second_row_button_y, 25, 25, WHITE, "F", BLACK),
    Button(10, second_row_button_y, 25, 25, PURPLE),
    Button(45, second_row_button_y, 25, 25, BROWN),
    Button(80, second_row_button_y, 25, 25, ORANGE),
    Button(115, second_row_button_y, 25, 25, GREY),
    Button(150, second_row_button_y, 25, 25, CYAN),
    Button(185, second_row_button_y, 25, 25, PEACH)
]

while running:
    clock.tick(FPS) #60 iterations per second
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running  = False

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            try:
                row, col = get_row_col_from_pos(pos)
                grid[row][col] = drawing_colour
            except IndexError:
                for button in buttons:
                    if not button.clicked(pos):
                        continue
                    
                    drawing_colour = button.colour

                    if button.text == "C":
                        grid = init_grid(ROWS, COLS, BG_COLOUR)
                        drawing_colour = BLACK

                    if button.text == "T":
                        if DRAW_GRID_LINES:
                            DRAW_GRID_LINES = False
                        else:
                            DRAW_GRID_LINES = True
                        drawing_colour = BLACK
                    
                    if button.text == "F":
                        #floorfill algorithm
                        drawing_colour = BLUE
                        flood_fill(WINDOW, drawing_colour)

                    

    draw(WINDOW, grid, buttons)

pygame.quit()

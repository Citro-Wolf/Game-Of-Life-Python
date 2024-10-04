import pygame, random, copy
def generateRandomCells():
    cells = []
    count = 0
    cellCount = 0
    for y in range(height // cellSize):
        cells.append([])
        for x in range(width // cellSize):
            if random.random() < 0.75:
                cells[y].append(True)
                count = count + 1
            else:
                cells[y].append(False)
            cellCount = cellCount + 1
    print(f"Percentage of Cells: {round((count / cellCount * 100), 2)}%")
    return cells
def gameOfLife():
    #tempGrid = cells[:],[:] # Shallow copy thing!
    tempGrid = copy.deepcopy(cells) # Copies the cells to RAM.
    for y in range(height // cellSize):
        for x in range(width // cellSize):
            aliveNeighbors = 0
            for localY in range(y-1, y+2):
                for localX in range(x-1,x+2):
                    if (localX == x) and (localY == y):
                        continue
                    elif cells[localY % (height // cellSize)][localX % (width // cellSize)]:
                        aliveNeighbors += 1
    ##### RULES #####                        
            if cells[y][x] and (aliveNeighbors < 2 or aliveNeighbors > 3):
                tempGrid[y][x] = False
            elif (not cells[y][x]) and aliveNeighbors == 3:
                tempGrid[y][x] = True
    
    return tempGrid
    ###### END ######
    
pygame.init()
running = True
### CONFIGURATION ###
width = 640
height = 480
cellSize = 5
framerate = 24
######## END ########
clock = pygame.time.Clock()
cells = generateRandomCells()
screen = pygame.display.set_mode((width, height))

while running:
    clock.tick(framerate)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0,0,0))

    for y in range(height // cellSize):
        for x in range(width // cellSize):
            if cells[y][x]:
                pygame.draw.rect(screen, (255,255,255), (x*cellSize, y*cellSize, cellSize, cellSize))

    #pygame.draw.rect(screen, (255,0,0), (width//2, height//2, 5,5))
    
    cells = gameOfLife()

    pygame.display.flip()
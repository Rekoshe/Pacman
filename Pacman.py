#imports
import pygame
import Map
import player
import Ghosts

#some variables
Blinkyvision = [0, 0]

score = -1

#setup
pygame.init()
pygame.font.init()
Fonts = pygame.font.SysFont('Arial', 20)
screen = pygame.display.set_mode((Map.mapWidth*Map.tileSize, Map.mapHeight*Map.tileSize))
pygame.display.set_caption("Pacman")
clock = pygame.time.Clock()
quits = False

#Ghosts
Ghostes = []
blink = Ghosts.Ghost("Blinky", Map.tileList[323][0], Map.tileList[323][1])
ink = Ghosts.Ghost("Inky", Map.tileList[321][0], Map.tileList[321][1])
Clyde = Ghosts.Ghost("Clyde", Map.tileList[320][0], Map.tileList[320][1])

Ghostes.append(blink)
Ghostes.append(ink)
Ghostes.append(Clyde)

for tile in Map.emptyList:
    if (tile[0] + Map.tileSize, tile[1]) not in Map.wallList and (tile[0], tile[1] + Map.tileSize) not in Map.wallList or (tile[0] - Map.tileSize, tile[1]) not in Map.wallList and (tile[0], tile[1] - Map.tileSize) not in Map.wallList or (tile[0] + Map.tileSize, tile[1]) not in Map.wallList and (tile[0], tile[1] - Map.tileSize) not in Map.wallList or (tile[0] - Map.tileSize, tile[1]) not in Map.wallList and (tile[0], tile[1] + Map.tileSize) not in Map.wallList:
        Map.nodesList.append(tile)



playerTargetTile = (Map.playerX, Map.playerY)


#gameloop
while not quits:
    #event handler
    key = ''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quits = True
        elif event.type == pygame.KEYDOWN:
            key = event.key

    #drawing stuff:
    screen.fill([0, 0, 0])
    for wall in Map.wallList:
        drs = (wall[0] -9, wall[1] -9, Map.tileSize, Map.tileSize)
        mp = pygame.draw.rect(screen, (0, 0, 255), drs)

    text = Fonts.render("score is: "+ str(score), True, (255, 255, 255))
    screen.blit(text, (Map.tileList[1][0], Map.tileList[1][1] - 14))
    #287

    #temporarly just for debuging
    for dots in Map.dotsList:
        pygame.draw.rect(screen, (255, 255, 0), (dots[0],dots[1] , 4, 4))
    #Calculating a node's weight
    Map.CalNodes()

    #pakistan man
    pakistan = pygame.draw.circle(screen, (255, 255, 0), (Map.playerX, Map.playerY), 8)

    #Ghosts
    Blinky = pygame.draw.circle(screen, (255, 0, 0), (blink.Xpos, blink.Ypos), 8)
    Inky = pygame.draw.circle(screen, (0, 0, 255), (ink.Xpos, ink.Ypos), 8)
    Clyder = pygame.draw.circle(screen, (255, 255, 0), (Clyde.Xpos, Clyde.Ypos), 8)

    for ghost in Ghostes:
        ghost.search()



    #handling button presses
    if key == pygame.K_RIGHT or key == pygame.K_LEFT:
        col = []
        colB = []
        for tile in Map.tileList:
            if tile[1] == Map.playerY and tile[0] > Map.playerX and key == pygame.K_RIGHT:
                col.append(tile)
            elif tile[1] == Map.playerY and tile[0] < Map.playerX and key == pygame.K_LEFT:
                col.append(tile)
        for tile in col:
            if tile in Map.wallList and col.index(tile) == 0 and key != pygame.K_LEFT:
                break
            elif tile in Map.wallList and col.index(tile) != 0 and key == pygame.K_RIGHT:
                playerTargetTile = (tile[0] - Map.tileSize, tile[1])
                break
            elif key == pygame.K_LEFT and tile in Map.wallList:
                colB.append(tile)
        else:
            if len(colB) != 0:
                playerTargetTile = (colB[-1][0] + Map.tileSize, colB[-1][1])

    if key == pygame.K_UP or key == pygame.K_DOWN:
        row = []
        rowB = []
        for tile in Map.tileList:
            if tile[0] == Map.playerX and tile[1] > Map.playerY and key == pygame.K_DOWN:
                row.append(tile)
            elif tile[0] == Map.playerX and tile[1] < Map.playerY and key == pygame.K_UP:
                row.append(tile)
        for tile in row:
            if tile in Map.wallList and row.index(tile) == 0 and key != pygame.K_UP:
                break
            elif tile in Map.wallList and row.index(tile) != 0 and key == pygame.K_DOWN:
                playerTargetTile = (tile[0], tile[1] - Map.tileSize)
                break
            elif key == pygame.K_UP and tile in Map.wallList:
                rowB.append(tile)
        else:
            if len(rowB) != 0:
                playerTargetTile = (rowB[-1][0], rowB[-1][1] + Map.tileSize)

    #movement
    if Map.playerX < playerTargetTile[0]:
        Map.playerX += 3
    elif Map.playerX > playerTargetTile[0]:
        Map.playerX -= 3
    elif Map.playerY < playerTargetTile[1]:
        Map.playerY += 3
    elif Map.playerY > playerTargetTile[1]:
        Map.playerY -= 3

    for ghost in Ghostes:
        if ghost.Xpos < ghost.target[0]:
            ghost.Xpos += 1
        elif ghost.Xpos > ghost.target[0]:
            ghost.Xpos -= 1
        elif ghost.Ypos < ghost.target[1]:
            ghost.Ypos += 1
        elif ghost.Ypos > ghost.target[1]:
            ghost.Ypos -= 1


    #eating dots
    if (Map.playerX, Map.playerY) in Map.dotsList:
        Map.dotsList.remove((Map.playerX, Map.playerY))
        score += 1

    #Updating the display
    pygame.display.update()
    clock.tick(30)

#quiting the game when the loop ends
print BlinkyTargetTile
pygame.quit()
quit()

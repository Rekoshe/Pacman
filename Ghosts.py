import Map


class Ghost(object):
    def __init__(self, Name, Xpos, Ypos):
        self.Name = Name
        self.Xpos = Xpos
        self.Ypos = Ypos
        self.target = (Xpos, Ypos)

    def search(self):
        if (self.Xpos, self.Ypos) in Map.nodesList:
            frontRow = []
            frontCol = []
            backRow = []
            backCol = []
            vision = []
            targets = []
            targeter = {}
            directs = [frontRow, frontCol]
            playerWeightDic = {}

            if self.Name == "Blinky":
                target = (Map.playerX, Map.playerY)
            elif self.Name == "Pinky":
                target = Map.playerTargetTile
            elif self.Name == "Inky":
                target = (Map.playerX - Map.tileSize*5, Map.playerY)
            elif self.Name == "Clyde":
                target = (Map.playerX + Map.tileSize*5, Map.playerY)

            for node in Map.nodesList:
                a = 0
                b = 0
                if node[0] > target[0]:
                    a = node[0] - target[0]
                elif node[0] < target[0]:
                    a = target[0] - node[0]
                if node[1] > target[1]:
                    b = node[1] - target[1]
                elif node[1] < target[1]:
                    b = target[1] - node[1]
                c = int(round((a**2 + b**2)**0.5))
                playerWeightDic[node] = c

            for tile in Map.tileList:
                if tile[1] == self.Ypos:
                    if tile[0] > self.Xpos:
                        frontRow.append(tile)
                    elif tile[0] < self.Xpos:
                        backRow.append(tile)
                elif tile[0] == self.Xpos:
                    if tile[1] > self.Ypos:
                        frontCol.append(tile)
                    elif tile[1] < self.Ypos:
                        backCol.append(tile)

            backRow = list(reversed(backRow))
            backCol = list(reversed(backCol))
            directs.append(backRow)
            directs.append(backCol)

            for lst in directs:
                for tile in lst:
                    if tile in Map.wallList:
                        ind = lst.index(tile)
                        del lst[ind:]
                        break
                for tile in lst:
                    if tile in Map.nodesList:
                        vision.append(tile)
                        break



            for nodes in vision:
                distance = int(round(((nodes[1] - self.Ypos)**2 + (nodes[0] - self.Xpos)**2)**0.5)) + playerWeightDic[nodes]
                targeter[distance] = nodes
                targets.append(distance)
                if len(targets) != 0:
                    targets.sort()
                    GhostTargetTile = targeter[targets[0]]
                    self.target = GhostTargetTile

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
                distance = int(round(((nodes[1] - self.Ypos)**2 + (nodes[0] - self.Xpos)**2)**0.5)) + Map.weightDic[nodes]
                targeter[distance] = nodes
                targets.append(distance)
            if len(targets) != 0:
                targets.sort()
                GhostTargetTile = targeter[targets[0]]
                self.target = GhostTargetTile


class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def aStar(maze, start, end):
    startNode = Node(None, start)
    endNode = Node(None, end)
    
    openList = []
    closedList = []

    openList.append(startNode)
    while openList:
        currentNode = openList[0]
        currentIdx = 0

        for index, item in enumerate(openList):
            if item.f < currentNode.f:
                currentNode = item
                currentIdx = index

        openList.pop(currentIdx)
        closedList.append(currentNode)

        if currentNode == endNode:
            path = []
            current = currentNode
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # reverse

        children = []
        for newPosition in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nodePosition = (
                currentNode.position[0] + newPosition[0],  # X
                currentNode.position[1] + newPosition[1])  # Y
                
            within_range_criteria = [
                nodePosition[0] > (len(maze) - 1),
                nodePosition[0] < 0,
                nodePosition[1] > (len(maze[len(maze) - 1]) - 1),
                nodePosition[1] < 0,
            ]

            if any(within_range_criteria): 
                continue
            if maze[nodePosition[0]][nodePosition[1]] != 0:
                continue

            new_node = Node(currentNode, nodePosition)
            children.append(new_node)
        for child in children:
            if child in closedList:
                continue

            child.g = currentNode.g + 1
            child.h = ((child.position[0] - endNode.position[0]) ** 2) + ((child.position[1] - endNode.position[1]) ** 2)            
            child.f = child.g + child.h

            cont = False
            for openNode in openList:
                if child == openNode and child.g > openNode.g > 0:
                    cont=True
                    break
            if cont:
                    continue
            if not child in openList:
                openList.append(child)

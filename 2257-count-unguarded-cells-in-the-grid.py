class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # probably easier to count guarded then subtract

        numSquares = m*n
        numGuards = len(guards)
        numWalls = len(walls)
        # set for guarded squares
        guarded = set()
        guardSet = set()
        for guard in guards:
            guarded.add((guard[0], guard[1]))
            guardSet.add((guard[0], guard[1]))
        wallSet = set()
        for wall in walls:
            guarded.add((wall[0], wall[1]))
            wallSet.add((wall[0], wall[1]))
        for guard in guards:
            pos = (guard[0], guard[1])

            # check south
            for down in range(pos[0] + 1, m):
                checkPos = (down, pos[1])
                # if line of sight is interrupted
                if checkPos in wallSet or checkPos in guardSet:
                    break
                # if checkPos is already in guarded, just doesn't do anything
                guarded.add(checkPos)

            #check north
            for up in range(pos[0] - 1, -1, -1):
                checkPos = (up, pos[1])
                if checkPos in wallSet or checkPos in guardSet:
                    break
                guarded.add(checkPos)

            #check east
            for right in range(pos[1] + 1, n):
                checkPos = (pos[0], right)
                if checkPos in wallSet or checkPos in guardSet:
                    break
                guarded.add(checkPos)

            #check west
            for left in range(pos[1] -1, -1, -1):
                checkPos = (pos[0], left)
                if checkPos in wallSet or checkPos in guardSet:
                    break
                guarded.add(checkPos)

        return numSquares - len(guarded)


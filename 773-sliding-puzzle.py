class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # I'm thinking brute force with caching... so like cache number of moves from a certain state
        # that might be expensive tho...
        target = "123450"
        
        def getStrFromBoard(board):
            pos = ""
            for i in range(len(board)):
                for num in board[i]:
                    pos += str(num)
            
            return pos
        
        startPos = getStrFromBoard(board)
        
        potentialMoves = {
            0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
            3: [0, 4], 4: [1, 3, 5], 5: [2, 4]
        }

        queue = collections.deque()
        visited = set()
        queue.append((startPos, 0))
        visited.add(startPos)

        while queue:
            state, moves = queue.popleft()

            if state == target:
                return moves

            i0 = state.index('0')

            for potentialMove in potentialMoves[i0]:
                new_state = list(state)
                new_state[i0], new_state[potentialMove] = new_state[potentialMove], new_state[i0]
                new_state_str = getStrFromBoard(new_state)

                if new_state_str not in visited:
                    visited.add(new_state_str)
                    queue.append((new_state_str, moves + 1))

        return -1
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # STACK PROBLEM - REMEMBER PATTERN FOR STACK PROBLEMS
        # Basically, think about the conditions when you add to a stack and when you
        # remove from it

        stack = []
        for num in asteroids:
            addToStack = True
            while stack:
                if num > 0:
                    break
                elif stack[-1] < 0:
                    break
                elif abs(num) > stack[-1]:
                    stack.pop(-1)
                elif abs(num) == stack[-1]:
                    stack.pop(-1)
                    addToStack = False
                    break
                else:
                    addToStack = False
                    break
            if addToStack:
                stack.append(num)
        return stack


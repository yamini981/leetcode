class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # need more practice with stacks
        # key is: think about how we can add values to a pile (stack)
        # that we can just pick up from when necessary and then update
        # the answer as needed 
        answer = [0] * len(temperatures)
        stack = []
        for i in range(len(answer)):
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                stackI = stack.pop(-1)
                answer[stackI] = i - stackI
            stack.append(i)
        return answer
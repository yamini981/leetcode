class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # find operator, then 2 nearest prev integers
        # stack problem
        numStack = []
        for i in range(len(tokens)):
            token = tokens[i]
            if token == "+":
                num1 = int(numStack.pop())
                num2 = int(numStack.pop())
                numStack.append(num2 + num1)
            elif token == "-":
                num1 = int(numStack.pop())
                num2 = int(numStack.pop())
                numStack.append(num2 - num1)
            elif token == "/":
                num1 = int(numStack.pop())
                num2 = int(numStack.pop())
                numStack.append(int(num2 / num1))
            elif token == "*":
                num1 = int(numStack.pop())
                num2 = int(numStack.pop())
                numStack.append(num2 * num1)
            else:
                numStack.append(token)
    
        return int(numStack[-1])
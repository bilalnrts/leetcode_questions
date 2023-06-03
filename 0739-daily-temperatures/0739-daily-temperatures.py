class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        myStack = []
        result = [0] * len(temperatures)
        
        for index, temp in enumerate(temperatures):
            while myStack and temp > myStack[-1][0]:
                stackTemp, stackIndex = myStack.pop()
                result[stackIndex] = index - stackIndex
            myStack.append([temp, index])
        return (result)
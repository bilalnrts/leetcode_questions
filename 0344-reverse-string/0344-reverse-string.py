class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.myFunc(s, len(s), 0)
    
    def myFunc(self, s, lenght, current : int):
        if (current == int(lenght / 2)):
            return
        s[current], s[-(current + 1)] = s[-(current + 1)], s[current]
        return self.myFunc(s, lenght, current + 1)
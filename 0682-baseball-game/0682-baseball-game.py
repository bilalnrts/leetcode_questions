class Solution:
    def __init__(self):
        self.mylist = []
    
    def ft_double(self):
        if (self.mylist != []):
            self.mylist.append(self.mylist[-1] * 2)
    
    def ft_cancel(self):
        if (self.mylist != []):
            self.mylist.pop()
    
    def ft_total_add(self):
        if (len(self.mylist) >= 2):
            last_index = len(self.mylist) -1
            self.mylist.append(self.mylist[last_index] + self.mylist[last_index - 1])
    
    def calPoints(self, operations: List[str]) -> int:
        for i in operations:
            if (i == "C" or i == "D" or i == "+"):
                if (i == "C"):
                    self.ft_cancel()
                elif (i == "D"):
                    self.ft_double()
                else:
                    self.ft_total_add()
            else:
                self.mylist.append(int(i))
        
        return sum(self.mylist)
        
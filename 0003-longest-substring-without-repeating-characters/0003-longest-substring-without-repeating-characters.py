class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (str):
            maxVal = 0
            count = 0
            i = 0
            mylist = []
            while (i < len(s)):
                if ((len(mylist) == 0) or (s[i] not in mylist)):
                    mylist.append(s[i])
                    count += 1
                    maxVal = max(maxVal, count)
                    i += 1
                elif (s[i] in mylist):
                    mylist = []
                    count = 0
                    i = self.helper_func(s, i) + 1
            return (maxVal)
    
    def helper_func(self, s1, index):
        i = index - 1
        while (i >= 0):
            if (s1[i] == s1[index]):
                return (i)
            i -= 1
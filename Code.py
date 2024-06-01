class Solution:
    def scoreOfString(self, s: str) -> int:
        l = [ord(x) for x in s]
        sum = 0
        for x in range(len(l)-1):
            sum+= abs(l[x]-l[x+1])
        return sum

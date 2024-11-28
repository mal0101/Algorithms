class Solution(object):
    
   def getRow(self, rowIndex):
        res = [1] * (rowIndex + 1)
        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                res[j] += res[j-1]
        return res
     
def main():
    print(Solution().getRow(5))
    
if __name__ == "__main__":
    main()
    
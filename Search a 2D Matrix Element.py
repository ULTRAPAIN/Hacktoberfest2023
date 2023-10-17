#Search a 2D Matrix Element

class Solution:
   def searchMatrix(self, matrix, target):
      try:
         length = len(matrix[0])
         counter1, counter2 = 0, length-1
         while True:
            if matrix[counter1][counter2] == target:
               return True
            elif matrix[counter1][counter2]>target:
               counter2-=1
               continue
            counter1 = counter1 + 1
            if counter1 >= len(matrix) or counter2<0:
               return False
         except:
            return False
ob1 = Solution()
print(ob1.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))

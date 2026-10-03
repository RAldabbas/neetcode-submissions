class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left1 = 0
        right1 = len(matrix) - 1
        left2 = 0
        right2 = len(matrix[0]) - 1

        while left1 <= right1:
            middle = (left1 + right1) // 2

            if target < matrix[middle][0]:
                right1 = middle - 1
            elif target > matrix[middle][-1]:
                left1 = middle + 1
            else:
                while left2 <= right2:
                    middle2 = (left2 + right2) // 2
                    if target > matrix[middle][middle2]:
                        left2 = middle2 + 1
                    elif target < matrix[middle][middle2]:
                        right2 = middle2 - 1
                    else:
                        if matrix[middle][middle2] == target:
                            return True
                return False
        return False
                        

        
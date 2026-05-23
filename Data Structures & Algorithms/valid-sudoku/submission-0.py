class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        blocks = defaultdict(list)
        cols = defaultdict(list)
        
        
        for r in range(9):
            for c in range(9):
                curr_val = board[r][c]
                cols[c].append(curr_val)
                blocks[(r // 3, c // 3)].append(curr_val)

        for row in board:
            if self.hasDupe(row):
                return False

        for col in cols.values():
            if self.hasDupe(col):
                return False
        
        print(blocks)
        for block in blocks.values():
            if self.hasDupe(block):
                return False
        return True
    
    def hasDupe(self, nums: List[str]) -> bool:
        seen = set()
        for num in nums:
            if num == ".":
                continue
            if num in seen:
                return True
            seen.add(num)
        return False
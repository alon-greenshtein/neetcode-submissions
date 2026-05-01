from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nums = defaultdict(bool)
        for x in range(1,10):
            nums[str(x)] = False

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif nums[board[i][j]] is True:
                    return False
                nums[board[i][j]] = True
            for k in nums:
                nums[k] = False
        
        for i in range(9):
            for j in range(9):
                if board[j][i] == ".":
                    continue
                elif nums[board[j][i]] is True:
                    return False
                nums[board[j][i]] = True
            for k in nums:
                nums[k] = False
        
        for a in range(3):
            for b in range(3):
                for i in range(3*a, 3*a+3):
                    for j in range(3*b,3*b+3):
                        if board[i][j] == ".":
                            continue
                        elif nums[board[i][j]] is True:
                            return False
                        nums[board[i][j]] = True
                for k in nums:
                    nums[k] = False

        return True

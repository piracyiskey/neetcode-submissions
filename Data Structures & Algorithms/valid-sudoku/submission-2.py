class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        boxes = defaultdict(set)

        for c in range(9):
            for r in range(9):
                if board[c][r] == ".":
                    continue
                elif (board[c][r] in rows[r] or
                     board[c][r] in cols[c] or
                     board[c][r] in boxes[c // 3, r // 3]):
                     return False
                else:
                    rows[r].add(board[c][r])
                    cols[c].add(board[c][r])
                    boxes[c // 3, r// 3].add(board[c][r])
        return True
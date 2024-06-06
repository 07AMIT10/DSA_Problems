class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     # validate rows
    #     for i in range(9):
    #         s = set()
    #         for j in range(9):
    #             item =  board[i][j]
    #             if item in s:
    #                 return False
    #             elif itmem not ".":
    #                 s.add(item)
        
    #     # validate cols
    #     for i in range(9):
    #         s = set()
    #         for j in range(9):
    #             item =  board[j][i]
    #             if item in s:
    #                 return False
    #             elif itmem not ".":
    #                 s.add(item)

    #     # validate boxes
    #     starts = [(0,0), (0,3), (0,6), 
    #     (3,0), (3,3), (3,6)
    #     (6,0), (6,3), (6,6)]

    #     for i, j in starts:
    #         s = set()
    #         for row in ragne(i, i+3):
    #             item = board[row][col]
    #             if item in s:
    #                 return False
    #             elif item != '.':
    #                 s.add(item)
    # return True
        
    # More consized solution
        row, col, block = set(),set(), set()
        for i in range(9):
            for j in range(9):
                if (board[i][j]!='.'):
                    r_key = (i, board[i][j])
                    c_key = (j, board[i][j])
                    b_key = (i//3, j//3, board[i][j])
                    if ((r_key in row) or (c_key in col) or (b_key in block)):
                        return False
                    row.add(r_key)
                    col.add(c_key)
                    block.add(b_key)
        return True
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #this checks for rows
        for i in range(9):
            row_set = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row_set:
                    return False
                row_set.add(board[i][j])
        
        #what logic would check for columns
        for i in range(9):
            col_set = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in col_set:
                    return False
                col_set.add(board[j][i])
        #now we have a row and col set filled and checked for dups
        #now we need ot check individual subsets
        for row_start in range(0,9,3):
            for col_start in range(0,9,3):
                sub_set = set()
                for i in range(row_start,row_start+3):
                    for j in range(col_start,col_start+3):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in sub_set:
                            return False
                        sub_set.add(board[i][j])
        
        return True

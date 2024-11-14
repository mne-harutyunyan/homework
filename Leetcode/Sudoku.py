def isValidSudoku(self, board: list[list[str]]) -> bool:
        def isValid(num):
            result = [x for x in num if x != "."]
            return len(set(result)) == len(result)
        for i in range(len(board)):
            if not isValid(board[i]):
                return False
            if not isValid([board[j][i] for j in range(len(board[i]))]):
                return False
        for row_box in range(3):
            for col_box in range(3):
                box = []
                for i in range(row_box * 3,row_box * 3 + 3):
                    for j in range(col_box * 3,col_box * 3 + 3):
                        box.append(board[i][j])
                if not isValid(box):
                    return False
        return True

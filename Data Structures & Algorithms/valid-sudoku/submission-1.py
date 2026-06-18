class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = set()
        colSet = []
        boxSet = []

        for i in range(len(board)):
            if i % 3 == 0:
                boxSet = []

            for j in range(len(board[i])):
                if i == 0:
                    colSet.append(set())

                if len(boxSet) == int(j / 3):
                    boxSet.append(set())

                #Columns
                if board[i][j] != '.':
                    if board[i][j] in colSet[j]:
                        return False
                    colSet[j].add(board[i][j])

                # Rows
                    if board[i][j] in rowSet:
                        return False
                    rowSet.add(board[i][j])

                # Boxes
                    if board[i][j] in boxSet[int(j / 3)]:
                        return False
                    boxSet[int(j / 3)].add(board[i][j])

            rowSet = set()

        return True
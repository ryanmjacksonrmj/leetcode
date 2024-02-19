class Solution(object):

# https://leetcode.com/problems/valid-sudoku/description/?source=submission-noac
# My solution is commented below. It doesn't work for the leetcode solution because my solution factors in numbers that aren't on the board as well as the ones that are. The uncommented solution below is an elegant solution from another user.

  # def isValidSudoku(self, board):
  #   row_number = 0
  #   column_set = []
  #   box_set = []
  #   for row in board:
  #     row_set = set()
  #     column_number = 0
  #     for column in row:
  #       if column != ".":
  #         column = int(column)
  #         if column in row_set:
  #           return False
  #         if not not column_set and (len(column_set) - 1) >= column_number and column in column_set[column_number]:
  #           return False
  #         if not not box_set and (len(box_set) - 1) >= ((column_number // 3) + (3 * (row_number // 3))) and column in box_set[(column_number // 3) + (3 * (row_number // 3))]:
  #           return False
  #         row_set.add(column)
  #         if (len(column_set) - 1) < column_number:
  #           column_set.append({column})
  #         else:
  #           column_set[column_number].add(column)
  #         if (len(box_set) -1) < ((column_number // 3) + (3 * (row_number // 3))):
  #           box_set.append({column})
  #         else:
  #           box_set[(column_number // 3) + (3 * (row_number // 3))].add(column)
  #       column_number += 1
  #     row_number += 1
  #   return True

    def isValidSudoku(self, board):
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        return len(res) == len(set(res))		

# board = [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]

board = [[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]

answer = Solution()
print (answer.isValidSudoku(board))    




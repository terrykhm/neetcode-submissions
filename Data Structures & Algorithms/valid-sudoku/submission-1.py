class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        gridSets = [set() for _ in range(9)]
        yAxisDigitsSet = [set() for _ in range(9)]

        for y in range(len(board)): 

            xAxisDigitsSet = set()
            for x in range(len(board[y])): 
                digit = board[y][x]
                if digit == ".":
                    continue
                    
                subBoxNum = self.getSubBoxPosition(x, y)

                # Check if digit exists in subbox
                if digit in gridSets[subBoxNum]:
                    return False
                else:
                    gridSets[subBoxNum].add(digit)

                # Check across
                if digit in xAxisDigitsSet:
                    return False
                else:
                    xAxisDigitsSet.add(digit)

                # Check down
                if digit in yAxisDigitsSet[x]:
                    return False
                else:
                    yAxisDigitsSet[x].add(digit)
        return True
            

    def getSubBoxPosition (self, x: int, y: int) -> int:
        yPos = y // 3
        xPos = x // 3
        
        return 3 * yPos + xPos

# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         from collections import defaultdict
#         rows = defaultdict(set)
#         columns = defaultdict(set)
#         boxes = defaultdict(set)
#         for row in range(9):
#             for column in range(9):
#                 value = board[row][column]
#                 box_key = (row // 3, column // 3)
#                 if value == '.':
#                     continue
#                 elif value in rows[row]:
#                     return False
#                 elif value in columns[column]:
#                     return False
#                 elif value in boxes[box_key]:
#                     return False
#                 else:
#                     rows[row].add(value)
#                     columns[column].add(value)
#                     boxes[box_key].add(value)
#         return True








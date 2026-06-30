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










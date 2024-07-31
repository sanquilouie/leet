from typing import List


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                self.rectangle[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]


class Test:
    def soli(self):
        pass

row1 = 0
col1 = 0
row2 = 3
col2 = 2
for i in range(row1, row2 + 1):
    for j in range(col1, col2 + 1):
        print(i,j)

rect = [[1,2,1],[4,3,4],[3,2,1],[1,1,1]]
sol = SubrectangleQueries(rect)
sol.getValue(rect,0, 2)
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
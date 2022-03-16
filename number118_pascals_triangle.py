class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if(numRows == 1):
            return [[1]]
        elif(numRows == 2):
            return [[1], [1, 1]]
        else:
            triangle = [[1], [1, 1]]
            for row in range(2, numRows):
                triangle.append([])
                for col in range(0, row+1):
                    if(col == 0 or col == row):
                        triangle[row].append(1)
                    else:
                        triangle[row].append(triangle[row-1][col-1] + triangle[row-1][col])
        
        return triangle
        

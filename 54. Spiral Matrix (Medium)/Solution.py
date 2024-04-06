class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:

        # One liner solution
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
        
        
        # Basic solution
        res = []
        while matrix:
            res.extend(matrix.pop(0))
            if not matrix or not matrix[0]:
                break       

            for r in matrix :
                res.append(r[-1])
                r.pop()

            res.extend(reversed(matrix.pop()))

            if not matrix or not matrix[0]:
                break

            for r in reversed(matrix):
                res.append(r[0])
                r.pop(0)
            
        return res 
        
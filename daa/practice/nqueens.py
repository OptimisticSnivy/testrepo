def nqueens(n):
    board = [["." for _ in range(n)] for _ in range(n)]
    results = []

    def is_safe(board, row, col):
        # Column
        for i in range(row):
            if board[i][col] == "Q":
                return False

        # Top-left Diagonal 
        for i,j in zip(range(row,-1,-1), range(col,-1,-1)):
            if board[i][j] == "Q":
                return False

        # Top-right Diagonal 
        for i,j in zip(range(row,-1,-1), range(col,n)):
            if board[i][j] == "Q":
                return False

        return True
    
    def backtrack(row):
        if row == n:
            solution = ["".join(row) for row in board]
            results.append(solution)
            return 
        
        for col in range(n):
            if is_safe(board,row,col):
                board[row][col] = "Q"
                backtrack(row+1)
                board[row][col] = "."

    backtrack(0)
    return results

# Example Usage
n = 8
solutions = nqueens(n)
print(solutions)

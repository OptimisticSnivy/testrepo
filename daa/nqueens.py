def solve_n_queens(n):
    # Initialize the board and result list
    board = [["." for _ in range(n)] for _ in range(n)]
    results = []
    
    def is_safe(board, row, col):
        # Check column
        for i in range(row):
            if board[i][col] == "Q":
                return False
        # Check diagonal (top-left)
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == "Q":
                return False
        # Check diagonal (top-right)
        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i][j] == "Q":
                return False
        return True
    
    def backtrack(row):
        if row == n:
            # Add a solution to the results
            solution = ["".join(row) for row in board]
            results.append(solution)
            return
        for col in range(n):
            if is_safe(board, row, col):
                # Place a queen and move to the next row
                board[row][col] = "Q"
                backtrack(row + 1)
                # Remove the queen (backtrack)
                board[row][col] = "."

    # Start the backtracking from the first row
    backtrack(0)
    return results

n = 3
solutions = solve_n_queens(n)
for solution in solutions:
    for row in solution:
        print(row)
    print()


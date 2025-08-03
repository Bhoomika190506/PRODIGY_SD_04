import tkinter as tk
from tkinter import messagebox

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    box_row, box_col = row // 3 * 3, col // 3 * 3
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False
    return True

def solve_sudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if solve_sudoku(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def read_board():
    board = []
    valid = True
    for i in range(9):
        row = []
        for j in range(9):
            val = entries[i][j].get().strip()
            if val == "":
                row.append(0)
                entries[i][j].config(bg="white")
            elif val.isdigit() and 1 <= int(val) <= 9:
                row.append(int(val))
                entries[i][j].config(bg="white")
            else:
                entries[i][j].config(bg="lightcoral")
                valid = False
        board.append(row)
    if not valid:
        messagebox.showerror("Invalid Input", "Please enter only numbers 1-9.")
        return None
    return board

def write_board(board):
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)
            entries[i][j].insert(0, str(board[i][j]))
            entries[i][j].config(bg="lightgreen")

def on_solve():
    board = read_board()
    if board and solve_sudoku(board):
        write_board(board)
        messagebox.showinfo("Sudoku Solved", "Puzzle solved successfully!")
    elif board:
        messagebox.showerror("Unsolvable", "No solution exists for the given puzzle.")

def on_clear():
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)
            entries[i][j].config(bg="white")

def validate_input(P):
    return P == "" or (P.isdigit() and 1 <= int(P) <= 9)

root = tk.Tk()
root.title("Sudoku Solver")
root.resizable(False, False)
root.configure(bg="white")

vcmd = (root.register(validate_input), '%P')
entries = []

frame = tk.Frame(root, bg="white")
frame.pack(padx=10, pady=10)

for i in range(9):
    row = []
    for j in range(9):
        e = tk.Entry(frame, width=2, font=('Arial', 18), justify='center',
                     validate="key", validatecommand=vcmd,
                     highlightthickness=1, highlightbackground="black")
        e.grid(row=i, column=j, padx=(2 if j % 3 == 0 else 1), pady=(2 if i % 3 == 0 else 1))
        row.append(e)
    entries.append(row)

btn_frame = tk.Frame(root, bg="white")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Solve", command=on_solve, bg="lightblue", font=("Arial", 12), width=10).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Clear", command=on_clear, bg="lightgray", font=("Arial", 12), width=10).pack(side=tk.LEFT, padx=5)

root.mainloop()

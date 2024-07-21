import tkinter as tk
from tkinter import Canvas

def read_input_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    # Read the first line for n, m, t, f
    n, m,t,f= map(int, lines[0].split())

    # Initialize the grid
    grid = []
    for line in lines[1:]:
        row = line.split()
        grid.append(row)
    
    return n, m, grid

def create_grid(canvas, n, m, grid, cell_size=40):
    for i in range(n):
        for j in range(m):
            value = grid[i][j]
            x0 = j * cell_size
            y0 = i * cell_size
            x1 = x0 + cell_size
            y1 = y0 + cell_size

            if value == '-1':
                color = 'grey'
            elif value == '0':
                color = 'white'
            elif value.isdigit():
                color = '#ADD8E6'
            elif value.startswith('S'):
                color = 'lightgreen'
            elif value.startswith('G'):
                color = 'lightcoral'
            elif value.startswith('F'):
                color = 'lightyellow'
            else:
                color = 'white'

            canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline='black')

            if  value not in ['-1', '0']:
                canvas.create_text(x0 + cell_size/2, y0 + cell_size/2, text=value, font=("Helvetica", 12))

def main():
    root = tk.Tk()
    root.title("Grid Display")

    # Read the input file and create the grid
    n, m, grid = read_input_file('inputGUI.txt')
    
    cell_size = 40
    canvas = Canvas(root, width=m*cell_size, height=n*cell_size)
    canvas.pack()
    
    create_grid(canvas, n, m, grid, cell_size)

    root.mainloop()

if __name__ == "__main__":
    main()

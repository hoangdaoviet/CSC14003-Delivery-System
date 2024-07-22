import tkinter as tk
from tkinter import Canvas


import tkinter as tk


class App:
    def __init__(self, root):
        def on_entry_click(event):
            if root.entry.get() == default_text:
                root.entry.delete(0, tk.END)
                root.entry.config(fg="black")

        def on_entry_focus_out(event):
            if root.entry.get() == "":
                root.entry.insert(0, default_text)
                root.entry.config(fg="gray")

        self.root = root
        self.root.geometry('450x450')
        self.root.title("Search project")
        
        default_text = "Enter relative path of file..."

        root.entry = tk.Entry(root, fg="gray", width=50, justify="center", bg="white", highlightbackground="#2F4F4F")
        root.entry.insert(0, default_text)
        root.entry.pack(pady=(50, 50))
        
        root.entry.bind("<FocusIn>", on_entry_click)
        root.entry.bind("<FocusOut>", on_entry_focus_out)  

        # Create a frame to hold the buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=(40, 40))

        # Create 4 buttons and add them to the frame
        self.connect_button = tk.Button(self.button_frame, text="show input", bg="#323232", fg="#FAFAFA", width=40, height=2, cursor="hand2")
        self.connect_button.pack(pady=(10, 10))

        self.result = tk.Button(self.button_frame, text="show path", bg="#323232", fg="#FAFAFA", width=40, height=2, cursor="hand2")
        self.result.pack(pady=(5, 5))

        self.step = tk.Button(self.button_frame, text="Step by step", bg="#323232", fg="#FAFAFA", width=40, height=2, cursor="hand2")
        self.step.pack(pady=(5, 5))

        self.exit = tk.Button(self.button_frame, text="Exit", bg="#323232", fg="#FAFAFA", width=40, height=2, cursor="hand2")
        self.exit.pack(pady=(5, 5))

    

       

        

    



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
    root = tk.Tk()
    app = App(root)
    root.mainloop()

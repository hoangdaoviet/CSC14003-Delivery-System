import tkinter as tk
from tkinter import Canvas

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry('450x450')
        self.root.title("Search project")
        self.filename = ''
        self.steps = []
        self.current_step = -1
        self.previous_step = None

        # Define size of graph
        self.main_frame = tk.Frame(self.root)
        self.input_frame = tk.Frame(self.root)
        self.path_frame = tk.Frame(self.root)
        self.step_by_step_frame = tk.Frame(self.root)
        self.default_text = "Enter relative path of file..."
        self.show_main_frame()

    def on_entry_click(self, event):
        if self.entry.get() == self.default_text:
            self.entry.delete(0, tk.END)
            self.entry.config(fg="black")

    def on_entry_focus_out(self, event):
        if self.entry.get() == "":
            self.entry.insert(0, self.default_text)
            self.entry.config(fg="gray")

    def show_main_frame(self):
        self.hidden_all_frame()
        self.main_frame.pack(expand=True, anchor='center')

        self.entry = tk.Entry(self.main_frame, fg="gray", width=50, justify="center", bg="white", highlightbackground="#2F4F4F")
        self.entry.insert(0, self.default_text)
        self.entry.pack(pady=(50, 50))

        self.entry.bind("<FocusIn>", self.on_entry_click)
        self.entry.bind("<FocusOut>", self.on_entry_focus_out)
        
        self.filename = self.entry.get()
        self.default_text = self.filename
        print(self.filename)
        # Create a frame to hold the buttons
        self.button_frame = tk.Frame(self.main_frame)
        self.button_frame.pack(pady=(40, 40))

        # Create 4 buttons and add them to the frame
        self.input_button = tk.Button(self.button_frame, text="show input", command=self.show_input, bg="#323232", fg="#FAFAFA", width=40, height=2, cursor="hand2")
        self.input_button.pack(pady=(5, 5))

        self.result = tk.Button(self.button_frame, text="show path", bg="#323232", fg="#FAFAFA", width=40, height=2, cursor="hand2")
        self.result.pack(pady=(5, 5))

        self.step = tk.Button(self.button_frame, text="Step by step", command=self.show_step_by_step, bg="#323232", fg="#FAFAFA", width=40, height=2, cursor="hand2")
        self.step.pack(pady=(5, 5))

        self.exit = tk.Button(self.button_frame, text="Exit", bg="#323232", fg="#FAFAFA", width=40, height=2, cursor="hand2", command=root.quit)
        self.exit.pack(pady=(5, 5))

    def create_grid(self, canvas, n, m, grid, cell_size=40):
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

                if value not in ['-1', '0']:
                    canvas.create_text(x0 + cell_size / 2, y0 + cell_size / 2, text=value, font=("Helvetica", 12))

    def hidden_all_frame(self):
        self.main_frame.pack_forget()
        self.step_by_step_frame.pack_forget()
        self.input_frame.pack_forget()
        self.path_frame.pack_forget()

    def clear_frame(self, frame):
        for child in frame.winfo_children():
            child.destroy()

    def show_input(self):
        self.hidden_all_frame()
        self.clear_frame(self.input_frame)
        self.input_frame.pack(expand=True, anchor='center')

        n, m, grid = read_input_file(self.filename)
        cell_size = 20
        canvas = Canvas(self.input_frame, width=m * cell_size, height=n * cell_size)
        canvas.pack()

        self.create_grid(canvas, n, m, grid, cell_size)

        self.button_frame_input = tk.Frame(self.input_frame)
        self.button_frame_input.pack(pady=(40, 40))
        self.back = tk.Button(self.button_frame_input, text="Back", command=self.show_main_frame, bg="#323232", fg="#FAFAFA", width=30, height=1, cursor="hand2")
        self.back.pack(pady=(5, 5))

    def show_step_by_step(self):
        self.hidden_all_frame()
        self.clear_frame(self.step_by_step_frame)
        self.step_by_step_frame.pack(expand=True, anchor='center')
        self.button_frame_step = tk.Frame(self.step_by_step_frame)

        self.button_frame_step.pack(anchor="w",pady=(20, 20))
        self.back_step = tk.Button(self.button_frame_step, text="Back", command=self.show_main_frame, bg="#323232", fg="#FAFAFA", width=10, height=1, cursor="hand2")
        self.back_step.pack(side = tk.LEFT, padx = (0, 5))

        self.steps = read_output_file('outputGUI.txt')
        print(self.steps)
        self.current_step = -1

        n, m, self.grid = read_input_file(self.filename)
        cell_size = 20
        self.canvas = Canvas(self.step_by_step_frame, width=m * cell_size, height=n * cell_size)
        self.canvas.pack()

        self.create_grid(self.canvas, n, m, self.grid, cell_size)

        self.button_frame_step_2 = tk.Frame(self.step_by_step_frame)
        self.button_frame_step_2.pack(pady=(40, 40))
        self.next_step_button = tk.Button(self.button_frame_step_2, text="Next Step", command=self.next_step, bg="#323232", fg="#FAFAFA", width=30, height=1, cursor="hand2")
        self.next_step_button.pack(side = tk.LEFT ,padx=(0, 3))
        self.auto_run_button = tk.Button(self.button_frame_step_2, text="Auto Run", command=self.auto_run, bg="#323232", fg="#FAFAFA", width=30, height=1, cursor="hand2")
        self.auto_run_button.pack(side = tk.RIGHT, padx=(8, 10))
        

    def next_step(self):
        if self.current_step < len(self.steps) - 1:
            
            self.current_step += 1
            i, j = self.steps[self.current_step]
            self.update_grid(i, j)
            self.previous_step = (i, j)


    def update_grid(self, i, j):
        cell_size = 20
        x0 = j * cell_size
        y0 = i * cell_size
        x1 = x0 + cell_size
        y1 = y0 + cell_size
        self.canvas.create_rectangle(x0, y0, x1, y1, fill='green', outline='black')
        self.canvas.create_text(x0 + cell_size / 2, y0 + cell_size / 2, text="S", font=("Helvetica", 12))
    
    def auto_run(self):
        self.running = True
        self.auto_run_steps()

    def auto_run_steps(self):
        if self.running and self.current_step < len(self.steps) - 1:
            self.next_step()
            self.root.after(500, self.auto_run_steps)

def read_input_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    # Read the first line for n, m, t, f
    n, m, t, f = map(int, lines[0].split())

    # Initialize the grid
    grid = []
    for line in lines[1:]:
        row = line.split()
        grid.append(row)

    return n, m, grid

def read_output_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    steps = []
    for line in lines:
        parts = line.strip().split()
        print(parts)
        for part in parts:
            if part.startswith('(') and part.endswith(')'):
                i, j = map(int, part[1:-1].split(','))
                print(i, j)
                steps.append((i, j))
    return steps

root = tk.Tk()
app = App(root)
root.mainloop()

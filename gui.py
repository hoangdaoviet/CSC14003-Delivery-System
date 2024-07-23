import tkinter as tk
from tkinter import Canvas, messagebox
import re
import os

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry('600x600')
        self.root.title("Search project")
        self.filename = ''
        self.steps = {}
        self.current_step = {}
        self.entities = []
        self.current_entity_index = 0

        # Define size of graph
        self.welcome_frame = tk.Frame(self.root)
        self.main_frame = tk.Frame(self.root)
        self.input_frame = tk.Frame(self.root)
        self.path_frame = tk.Frame(self.root)
        self.step_by_step_frame = tk.Frame(self.root)
        self.choose_algorithm_frame = tk.Frame(self.root)
        self.default_text = "Enter relative path of file..."
        self.show_welcome_frame()

    def on_entry_click(self, event):
        if self.entry.get() == self.default_text:
            self.entry.delete(0, tk.END)
            self.entry.config(fg="black")

    def on_entry_focus_out(self, event):
        if self.entry.get() == "":
            self.entry.insert(0, self.default_text)
            self.entry.config(fg="gray")

    def show_welcome_frame(self):
        self.hidden_all_frame()
        self.clear_frame(self.welcome_frame)
        self.welcome_frame.pack(expand=True, anchor='center')

        self.label = tk.Label(self.welcome_frame, text="Welcome to the search project", font=("Helvetica", 16), fg="black")
        self.label.pack(pady=(20, 20))

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(pady=80, padx=30, fill='x')

        self.entry_frame = tk.Frame(self.main_frame, bg="white")
        self.entry_frame.pack(pady=(40, 40), fill='x')


        # Tạo entry và đặt nó trong frame con
        self.entry = tk.Entry(self.entry_frame, fg="gray", width=50, justify="left", bg="white", highlightbackground="#2F4F4F")
        self.entry.insert(0, "Enter relative path of file...")
        self.entry.pack(side='left', padx=(0, 5), fill='x', expand=True)


        self.entry.bind("<FocusIn>", self.on_entry_click)
        self.entry.bind("<FocusOut>", self.on_entry_focus_out)

        # Tạo button Enter và đặt nó trong frame con
        self.button_enter_input = tk.Button(self.entry_frame, text="Enter", command=self.enter_input, bg="#323232", fg="#FAFAFA", width=10, height=1, cursor="hand2")
        self.button_enter_input.pack(side='right')

        # Tạo button Exit và đặt nó dưới frame con
        self.button_exit = tk.Button(self.main_frame, text="Exit", command=root.quit, bg="#323232", fg="#FAFAFA", width=10, height=1, cursor="hand2")
        self.button_exit.pack(pady=(10, 40))

        

    def show_main_frame(self):
        self.hidden_all_frame()
        self.clear_frame(self.main_frame)
        self.main_frame.pack(expand=True, anchor='center')

        self.button_mainframe = tk.Frame(self.main_frame)
        self.button_mainframe.pack(pady=(40, 40))

        # Create 4 buttons and add them to the frame
        self.input_button = tk.Button(self.button_mainframe, text="show input", command=self.show_input, bg="#323232", fg="#FAFAFA", width=40, height=2, cursor="hand2")
        self.input_button.pack(pady=(5, 5))

        self.result = tk.Button(self.button_mainframe, text="show path", bg="#323232", fg="#FAFAFA", width=40, height=2, cursor="hand2")
        self.result.pack(pady=(5, 5))

        self.step = tk.Button(self.button_mainframe, text="Step by step", command=self.show_step_by_step, bg="#323232", fg="#FAFAFA", width=40, height=2, cursor="hand2")
        self.step.pack(pady=(5, 5))

        self.exit_main = tk.Button(self.button_mainframe, text="Back", bg="#323232", fg="#FAFAFA", width=40, height=2, cursor="hand2", command=self.show_welcome_frame)
        self.exit_main.pack(pady=(5, 5))

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
        self.welcome_frame.pack_forget()

    def clear_frame(self, frame):
        for child in frame.winfo_children():
            child.destroy()

    def enter_input(self):
        self.filename = self.entry.get()
        if self.check_file_exists(self.filename):
            self.default_text = self.filename
            self.show_main_frame()
        #self.default_text = self.filename
        else:
            messagebox.showerror("Error", "File not found. Please enter a valid file path.")
        #self.show_main_frame()
    def check_file_exists(self, filename):
        return os.path.isfile(filename)
    
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

        self.steps = read_output_file('outputGUI1.txt')
        print(self.steps)
        
        self.entities = list(self.steps.keys())
        self.current_step = {entity: -1 for entity in self.entities}

        print(f"Entities: {self.entities}")
        
        n, m, self.grid = read_input_file(self.filename)
        if not self.entities:
            self.label = tk.Label(self.step_by_step_frame, text="No solution", font=("Helvetica", 16), fg="black")
            self.label.pack(pady=(20, 20))
        else:
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
        if not self.entities:
            return

        entity = self.entities[self.current_entity_index]
        if self.current_step[entity] < len(self.steps[entity]) - 1:
            self.current_step[entity] += 1
            i, j = self.steps[entity][self.current_step[entity]]
            self.update_grid(i, j, entity)
        
        self.current_entity_index = (self.current_entity_index + 1) % len(self.entities)

    def update_grid(self, i, j, entity):
        cell_size = 20
        x0 = j * cell_size
        y0 = i * cell_size
        x1 = x0 + cell_size
        y1 = y0 + cell_size
        self.canvas.create_rectangle(x0, y0, x1, y1, fill='green', outline='black')
        self.canvas.create_text(x0 + cell_size / 2, y0 + cell_size / 2, text=entity, font=("Helvetica", 12))

    def auto_run(self):
        if not self.entities:
            return
        
        while any(self.current_step[entity] < len(self.steps[entity]) - 1 for entity in self.entities):
            self.next_step()
            self.root.update()
            self.root.after(500) # 500 milliseconds delay between steps

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
    steps = {}
    current_key = None

    with open(filename, 'r') as f:
        lines = f.readlines()

    for line in lines:
        parts = line.strip()

        # Check if this line is an entity identifier like "S", "S1", etc.
        if re.match(r'^\w+$', parts):
            current_key = parts
            steps[current_key] = []
        else:
            # Line is a series of coordinates, e.g., "(1, 1) (2, 1)"
            matches = re.findall(r'\((\d+),\s*(\d+)\)', parts)
            if matches and current_key:
                for match in matches:
                    i, j = int(match[0]), int(match[1])
                    steps[current_key].append((i, j))
            else:
                print(f"No matches found in line: {line}")

    if not steps:
        print("No steps parsed from the output file.")
    else:
        print(f"Parsed steps: {steps}")

    return steps

root = tk.Tk()
app = App(root)
root.mainloop()

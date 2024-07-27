import tkinter as tk
from tkinter import Canvas, messagebox, StringVar
import re
import os
import random
from board import Board 
from agent import *

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry('600x600')
        self.root.title("Search project")
        self.filename = ''
        self.algorithm_level1 = ''
        self.steps = {}
        self.current_step = {}
        self.entities = []
        self.current_entity_index = 0
        self.array_color = {}
        # Define size of graph
        self.welcome_frame = tk.Frame(self.root)
        self.main_frame = tk.Frame(self.root)
        self.input_frame = tk.Frame(self.root)
        self.path_frame = tk.Frame(self.root)
        self.step_by_step_frame = tk.Frame(self.root)
        self.choose_algorithm_frame = tk.Frame(self.root)
        self.default_text = "Enter relative path of file..."
        self.level = 0
        
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
        self.input_button = tk.Button(self.button_mainframe, text="Show input", command=self.show_input, bg="#323232", fg="#FAFAFA", width=40, height=2, cursor="hand2")
        self.input_button.pack(pady=(5, 5))

        self.result = tk.Button(self.button_mainframe, text="Show path",command= self.show_path_frame, bg="#323232", fg="#FAFAFA", width=40, height=2, cursor="hand2")
        self.result.pack(pady=(5, 5))

        self.step = tk.Button(self.button_mainframe, text="Step by step", command=self.show_step_by_step, bg="#323232", fg="#FAFAFA", width=40, height=2, cursor="hand2")
        self.step.pack(pady=(5, 5))

        if self.filename[12] == '1':
            self.exit_main = tk.Button(self.button_mainframe, text="Back", bg="#323232", fg="#FAFAFA", width=40, height=2, cursor="hand2", command=self.show_choose_algorithm_frame)
            self.exit_main.pack(pady=(5, 5))
        else:
            self.exit_main = tk.Button(self.button_mainframe, text="Back", bg="#323232", fg="#FAFAFA", width=40, height=2, cursor="hand2", command=self.show_welcome_frame)
            self.exit_main.pack(pady=(5, 5))
        
    def show_choose_algorithm_frame(self):
        self.hidden_all_frame()
        self.clear_frame(self.choose_algorithm_frame)
        self.choose_algorithm_frame.pack(expand=True, anchor='center')
        
        print('show_choose_algorithm_frame')
        self.button_choose = tk.Frame(self.choose_algorithm_frame)
        self.button_choose.pack(pady = (40,40))

        self.BFS_button = tk.Button(self.button_choose, text="BFS", bg="#323232", fg="#FAFAFA", width=40, height=2, cursor="hand2", command=lambda:self.set_algorithm_level1('BFS'))
        self.BFS_button.pack(pady=(5, 5))
        self.DFS_button = tk.Button(self.button_choose, text="DFS", bg="#323232", fg="#FAFAFA", width=40, height=2, cursor="hand2", command=lambda:self.set_algorithm_level1('DFS'))
        self.DFS_button.pack(pady=(5, 5))
        self.UCS_button = tk.Button(self.button_choose, text="UCS", bg="#323232", fg="#FAFAFA", width=40, height=2, cursor="hand2", command=lambda:self.set_algorithm_level1('UCS'))
        self.UCS_button.pack(pady=(5, 5))
        self.GBFS_button = tk.Button(self.button_choose, text="GBFS", bg="#323232", fg="#FAFAFA", width=40, height=2, cursor="hand2", command=lambda:self.set_algorithm_level1('GBFS'))
        self.GBFS_button.pack(pady=(5, 5))
        self.Astar_button = tk.Button(self.button_choose, text="A*", bg="#323232", fg="#FAFAFA", width=40, height=2, cursor="hand2", command=lambda:self.set_algorithm_level1('Astar'))
        self.Astar_button.pack(pady=(5, 5))

        self.back = tk.Button(self.button_choose, text="Back", bg="#323232", fg="#FAFAFA", width=40, height=2, cursor="hand2", command=self.show_welcome_frame)
        self.back.pack(pady=(5, 5))
        

    def show_path_frame(self):
        self.hidden_all_frame()
        self.clear_frame(self.path_frame)
        self.path_frame.pack(expand=True, anchor='center')

        paths, search_board = self.get_path()
        n, m, grid ,t,f= read_input_file(self.filename)
        grid = search_board if search_board else grid

        canvas = Canvas(self.path_frame, width=m * 40, height=n * 40)
        canvas.pack()

        self.create_grid(canvas, n, m, grid)

        
        # outputFilename = 'output' + self.filename[5:]
        # if self.filename[12] == '1':
        #     paths = read_output_file_level1(outputFilename, self.algorithm_level1)
        # else:
        #     paths = read_output_file(outputFilename)

        if paths:
            
            for entity, path in paths.items():
                if entity == 'S':
                    color = '#00FF00'
                else:
                    color = f'#{random.randint(0, 0xFFFFFF):06x}'
                for i in range(1, len(path)):
                    x0 = path[i-1][1] * 40 + 20
                    y0 = path[i-1][0] * 40 + 20
                    x1 = path[i][1] * 40 + 20
                    y1 = path[i][0] * 40 + 20
                    canvas.create_line(x0, y0, x1, y1, fill=color, width=2)

                

        button_back = tk.Button(self.path_frame, text="Back", command=self.show_main_frame, bg="#323232", fg="#FAFAFA", width=30, height=1, cursor="hand2")
        button_back.pack(pady=10)

    def set_algorithm_level1(self, algorithm):
        self.algorithm_level1 = algorithm

        self.show_main_frame()
        
        
    

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
                    pass
                    canvas.create_text(x0 + cell_size / 2, y0 + cell_size / 2, text=value, font=("Helvetica", 12))

    def hidden_all_frame(self):
        self.main_frame.pack_forget()
        self.step_by_step_frame.pack_forget()
        self.input_frame.pack_forget()
        self.path_frame.pack_forget()
        self.welcome_frame.pack_forget()
        self.choose_algorithm_frame.pack_forget()

    def clear_frame(self, frame):
        for child in frame.winfo_children():
            child.destroy()

    def enter_input(self):
        self.filename = self.entry.get()
        if self.check_file_exists(self.filename):
            self.default_text = self.filename
            print(self.filename[12])
            if self.filename[12] == '1':
                self.show_choose_algorithm_frame()
            else:
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
        
        

        n, m, grid, t, f = read_input_file(self.filename)

        if self.filename[12] != '1':
            time_var = StringVar()
            time_var.set(f"Time limit: {t}")

            self.label = tk.Label(self.input_frame, textvariable= time_var, font=("Helvetica", 14), fg="black")
            self.label.pack(pady=(10, 10))
            
            if self.filename[12] != '2':
                fuel_var = StringVar()
                fuel_var.set(f"Fuel limit: {f}")

                self.label = tk.Label(self.input_frame, textvariable= fuel_var, font=("Helvetica", 14), fg="black")
                self.label.pack(pady=(5, 5))
        cell_size = 40
        canvas = Canvas(self.input_frame, width=m * cell_size, height=n * cell_size)
        canvas.pack()
        

        self.create_grid(canvas, n, m, grid, cell_size)

        self.button_frame_input = tk.Frame(self.input_frame)
        self.button_frame_input.pack(pady=(30, 30))
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

        

        self.steps, search_board = self.get_path()
        # outputFilename = 'output' + self.filename[5:]
        # if self.filename[12] == '1':
        #     self.steps = read_output_file_level1(outputFilename, self.algorithm_level1)
        # else:
        #     self.steps = read_output_file(outputFilename)
        # print(self.steps)

        for entity in self.steps.keys():
            if entity == 'S':
                color = '#00FF00'
            else:
                color = f'#{random.randint(0, 0xFFFFFF):06x}'
                while color == '#00FF00':
                    color = f'#{random.randint(0, 0xFFFFFF):06x}'
            self.array_color[entity] = color
            self.array_color[f'{entity}_dark'] = self.darken_color(color)
                
        
        self.entities = list(self.steps.keys())
        self.current_step = {entity: -1 for entity in self.entities}

        print(f"Entities: {self.entities}")
        
        n, m, self.grid,t,f= read_input_file(self.filename)
        if not self.entities:
            self.label = tk.Label(self.step_by_step_frame, text="No solution", font=("Helvetica", 16), fg="black")
            self.label.pack(pady=(20, 20))
        else:
            cell_size = 40
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

    def check_override(self, i, j, entity):
        for index in range(self.current_step[entity]):
            if i == self.steps[entity][index][0] and j == self.steps[entity][index][1]:
                return True
        return False

    def update_grid(self, i, j, entity):
        cell_size = 40
        x0 = j * cell_size
        y0 = i * cell_size
        x1 = x0 + cell_size
        y1 = y0 + cell_size

        previous_step = self.current_step[entity] - 1
        #print(previous_step)
        if previous_step >= 0:
            if self.level == 4:
                gx_0 = self.steps[entity][previous_step][1] * cell_size
                gy_0 = self.steps[entity][previous_step][0] * cell_size
                gx_1 = gx_0 + cell_size
                gy_1 = gy_0 + cell_size
                if self.grid[self.steps[entity][previous_step][0]][self.steps[entity][previous_step][1]][0] == 'G':
                    self.canvas.create_rectangle(gx_0, gy_0, gx_1, gy_1, fill='lightcoral', outline='black')
                    self.canvas.create_text(gx_0 + cell_size / 2, gy_0 + cell_size / 2, text=self.grid[self.steps[entity][previous_step][0]][self.steps[entity][previous_step][1]], font=("Helvetica", 12))
                elif self.grid[self.steps[entity][previous_step][0]][self.steps[entity][previous_step][1]][0] == 'F':
                    self.canvas.create_rectangle(gx_0, gy_0, gx_1, gy_1, fill='lightyellow', outline='black')
                    self.canvas.create_text(gx_0 + cell_size / 2, gy_0 + cell_size / 2, text=self.grid[self.steps[entity][previous_step][0]][self.steps[entity][previous_step][1]], font=("Helvetica", 12))
                elif self.grid[self.steps[entity][previous_step][0]][self.steps[entity][previous_step][1]][0] == 'S':
                    self.canvas.create_rectangle(gx_0, gy_0, gx_1, gy_1, fill=self.array_color[entity], outline='black')
                    self.canvas.create_text(gx_0 + cell_size / 2, gy_0 + cell_size / 2, text=self.grid[self.steps[entity][previous_step][0]][self.steps[entity][previous_step][1]], font=("Helvetica", 12))
                elif self.grid[self.steps[entity][previous_step][0]][self.steps[entity][previous_step][1]] != '0':
                    self.canvas.create_rectangle(gx_0, gy_0, gx_1, gy_1, fill='#ADD8E6', outline='black')
                    self.canvas.create_text(gx_0 + cell_size / 2, gy_0 + cell_size / 2, text=self.grid[self.steps[entity][previous_step][0]][self.steps[entity][previous_step][1]], font=("Helvetica", 12))
                else:
                    self.canvas.create_rectangle(gx_0, gy_0, gx_1, gy_1, fill='white', outline='black')
                    
        if len(entity) > 1:
            if self.check_override(i,j,entity) and self.level != 4:
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=self.array_color[f'{entity}_dark'], outline='black')
            else:
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=self.array_color[entity], outline='black')
        else:
            if self.check_override(i,j,entity) and self.level != 4:
                self.canvas.create_rectangle(x0, y0, x1, y1, fill='#00AA00', outline='black')
            else:
                self.canvas.create_rectangle(x0, y0, x1, y1, fill='#00FF00', outline='black')
        self.canvas.create_text(x0 + cell_size / 2, y0 + cell_size / 2, text=entity, font=("Helvetica", 12))

    def auto_run(self):
        if not self.entities:
            return
        
        while any(self.current_step[entity] < len(self.steps[entity]) - 1 for entity in self.entities):
            self.next_step()
            self.root.update()
            self.root.after(500) # 500 milliseconds delay between steps

    def get_path(self):
        board = Board(self.filename)
        if self.filename[12] == '1':
            agent = PlayerLvl1()
            if self.algorithm_level1 == 'BFS':
                path = agent.BFS(board)
            elif self.algorithm_level1 == 'DFS':
                path = agent.DFS(board)
            elif self.algorithm_level1 == 'UCS':
                path = agent.UCS(board)
            elif self.algorithm_level1 == 'GBFS':
                path = agent.GBFS(board)
            elif self.algorithm_level1 == 'Astar':
                path = agent.AStar(board)
            self.level = 1
            search_board = None
        
        elif self.filename[12] == '2':
            agent = PlayerLvl2(board.t)
            path = agent.move(board)
            self.level = 2
            search_board = None
        elif self.filename[12] == '3':
            agent = PlayerLvl3(board.t, board.f)
            path = agent.move(board)
            self.level = 3
            search_board = None
        else:
            agent = PlayerLvl4(board.t, board.f)
            path, search_board = agent.move(board)
            self.level = 4
            # path = read_output_file('output' + self.filename[5:])
        return path, search_board
    
    def darken_color(self, color, factor=0.7):
        """ Darken the given color by a specified factor. """
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)
        
        r = int(r * factor)
        g = int(g * factor)
        b = int(b * factor)
        
        return f'#{r:02x}{g:02x}{b:02x}'

def blend_colors(color1, color2):
    # Convert colors to RGB
    r1, g1, b1 = int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:], 16)
    r2, g2, b2 = int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:], 16)

        # Blend the colors
    r = (r1 + r2) // 2
    g = (g1 + g2) // 2
    b = (b1 + b2) // 2

        # Return the blended color as a hex string
    return f'#{r:02x}{g:02x}{b:02x}'

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

    return n, m, grid, t, f

# def read_output_file(filename):
#     steps = {}
#     current_key = None

#     with open(filename, 'r') as f:
#         lines = f.readlines()

#     for line in lines:
#         parts = line.strip()

#         # Check if this line is an entity identifier like "S", "S1", etc.
#         if re.match(r'^\w+$', parts):
#             current_key = parts
#             steps[current_key] = []
#         else:
#             # Line is a series of coordinates, e.g., "(1, 1) (2, 1)"
#             matches = re.findall(r'\((\d+),\s*(\d+)\)', parts)
#             if matches and current_key:
#                 for match in matches:
#                     i, j = int(match[0]), int(match[1])
#                     steps[current_key].append((i, j))
#             else:
#                 print(f"No matches found in line: {line}")

#     if not steps:
#         print("No steps parsed from the output file.")
#     else:
#         print(f"Parsed steps: {steps}")

#     return steps

# def read_output_file_level1(filename, algorithm):
#     steps = {}
#     current_key = None

#     with open(filename, 'r') as f:
#         lines = f.readlines()

#     for i in range(len(lines)):
#         if lines[i].startswith(algorithm):
#             for j in range(i + 1, i + 3):
#                 parts = lines[j].strip()
#                 if parts == '-1':
#                     break
#         # Check if this line is an entity identifier like "S", "S1", etc.
#                 if re.match(r'^\w+$', parts):
#                     current_key = parts
#                     steps[current_key] = []
#                 else:
#                     # Line is a series of coordinates, e.g., "(1, 1) (2, 1)"
#                     matches = re.findall(r'\((\d+),\s*(\d+)\)', parts)
#                     if matches and current_key:
#                         for match in matches:
#                             i, j = int(match[0]), int(match[1])
#                             steps[current_key].append((i, j))
#                     else:
#                         print(f"No matches found in line: {lines[j]}")

#     if not steps:
#         print("No steps parsed from the output file.")
#     else:
#         print(f"Parsed steps: {steps}")

#     return steps
#steps = read_output_file_level1('outputGUI1.txt', 'DFS')
#print(steps)
root = tk.Tk()
app = App(root)
root.mainloop()
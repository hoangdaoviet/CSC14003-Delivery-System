import tkinter as tk
from tkinter import Canvas


import tkinter as tk


class App:
    def __init__(self, root):
        
        self.root = root
        self.root.geometry('450x450')
        self.root.title("Search project")
        self.filename = ''

        #define size of graph
        self.main_frame = tk.Frame(self.root)
        self.input_frame = tk.Frame(self.root)
        self.path_frame = tk.Frame(self.root)
        self.step_by_step_frame = tk.Frame(self.root)
        self.default_text = "Enter relative path of file..."
        self.show_main_frame()

        

    def on_entry_click(self,event):
        if self.entry.get() == self.default_text:
            self.entry.delete(0, tk.END)
            self.entry.config(fg="black")

    def on_entry_focus_out(self,event):
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

        # Create a frame to hold the buttons
        self.button_frame = tk.Frame(self.main_frame)
        self.button_frame.pack(pady=(40, 40))

        # Create 4 buttons and add them to the frame
        self.input_button = tk.Button(self.button_frame, text="show input",command= self.show_input, bg="#323232", fg="#FAFAFA", width=40, height=2, cursor="hand2")
        self.input_button.pack(pady=(10, 10))

        self.result = tk.Button(self.button_frame, text="show path", bg="#323232", fg="#FAFAFA", width=40, height=2, cursor="hand2")
        self.result.pack(pady=(5, 5))

        self.step = tk.Button(self.button_frame, text="Step by step", bg="#323232", fg="#FAFAFA", width=40, height=2, cursor="hand2")
        self.step.pack(pady=(5, 5))

        self.exit = tk.Button(self.button_frame, text="Exit", bg="#323232", fg="#FAFAFA", width=40, height=2, cursor="hand2")
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

                if  value not in ['-1', '0']:
                    canvas.create_text(x0 + cell_size/2, y0 + cell_size/2, text=value, font=("Helvetica", 12))
        
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
        self.filename = self.entry.get()
        self.default_text = self.filename
        
        n, m, grid = read_input_file(self.filename)
        cell_size = 20
        canvas = Canvas(self.input_frame, width= m*cell_size, height=n*cell_size)
        canvas.pack()
    
        self.create_grid(canvas, n, m, grid, cell_size)

        self.button_frame_2 = tk.Frame(self.input_frame)
        self.button_frame_2.pack(pady=(40, 40))
        self.back = tk.Button(self.button_frame_2, text="Back",command=self.show_main_frame, bg="#323232", fg="#FAFAFA", width=30, height=1, cursor="hand2")
        self.back.pack(pady=(5, 5))
        


    


    

       

        

    



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



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

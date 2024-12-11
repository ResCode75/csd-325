# Rachel Shaw - 10.2 assignment -  12/11/2024 
import tkinter as tk
import tkinter.messagebox as msg
from tkinter import Menu

class Todo(tk.Tk):
    def __init__(self, tasks=None):
        
        #Create Empty list
        super().__init__()
        if not tasks:
            self.tasks = [] # Empty list
        else:
            self.tasks = tasks
        

        # Menu and exit button 
        menu_bar = Menu(self)
        file_menu = Menu(menu_bar, tearoff = 0)
        menu_bar.add_cascade(label = "File", menu = file_menu)
        file_menu.add_command(label="Exit", command=self.destroy)
        self.config(menu=menu_bar)

        # define canvas that can scroll
        self.tasks_canvas = tk.Canvas(self)

        # define frames for tasks and entry box
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)

        # Set up scroll bar
        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview)
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        #Set size and title of window 
        self.title("Shaw To-Do App")
        self.geometry("300x400")

        # put frames and canvas where they're supposed to be
        self.task_create = tk.Text(self.text_frame, height = 3, bg = "white", fg="black")
        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas_frame = self.tasks_canvas.create_window((0,0), window=self.tasks_frame, anchor="n")
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill = tk.X) 
        self.task_create.focus_set()


       

        #Create task for direction
        todo1 = tk.Label(self.tasks_frame, text = "--- Add Items here. Right click to delete a task ---", bg= "SkyBlue1", fg="white", pady=10)
        todo1.bind("<Button-3>", self.remove_task)
        self.tasks.append(todo1)

        # Pack all tasks
        for task in self.tasks:
            task.pack(side = tk.TOP, fill=tk.X)

        #Keybinds
        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>", self.task_width)
    
        #Define app color scheme
        self.colour_schemes = [{"bg" : "SkyBlue1", "fg" : "white"}, {"bg" : "sandy brown", "fg" : "white"}]


    def add_task(self, event=None):
        # Retrieves input from the text box (1.0 means start at first character)
        task_text = self.task_create.get(1.0,tk.END).strip()
        
        if len(task_text) > 0:
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)
            self.set_task_colour(len(self.tasks), new_task)

            new_task.bind("<Button-3>", self.remove_task)
            new_task.pack(side=tk.TOP, fill=tk.X)

            self.tasks.append(new_task)
        
        # Clears text entry box
        self.task_create.delete(1.0, tk.END)

    # Creates message asking user if they'd really like to delete a task
    def remove_task(self, event):
        task = event.widget

        if msg.askyesno("Really Delete?", "Delete " + task.cget("text") + "?"):
            self.tasks.remove(event.widget)
            event.widget.destroy()
            self.recolour_tasks()
    
    #Recolour tasks after task deletion
    def recolour_tasks(self):
        # "Enumerate" = renumber tasks to define even and odd number tasks
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)
    
    # Allows colors to alternate using the remainder of the divmod function to index colour_schemes
    def set_task_colour(self, position, task):
        _, task_style_choice = divmod(position, 2)

        my_scheme_choice = self.colour_schemes[task_style_choice]
        task.configure(bg = my_scheme_choice["bg"])
        task.configure(fg = my_scheme_choice["fg"])
    
    # Makes tasks canvas scrollable
    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion = self.tasks_canvas.bbox("all"))
    
    #Makes sure tasks fill width of canvas
    def task_width(self, event):
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width = canvas_width)
    
    # moves canvas up and down for scrolling function
    def mouse_scroll(self, event):
        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        else:
            if event.num == 5:
                move= 1
            else:
                move= -1
            
            self.tasks_canvas.yview_scroll(move, "units")

if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()
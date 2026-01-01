import tkinter as tk

root = tk.Tk()

class Application:
    def __init__(self, root, name):
        
        self.root = root
        self.name = name
        
        self.screen(self.name)
        self.screenFrames()
        self.createButtons()

    def screen(self, name):
        self.root.title(name)
        self.root.configure(bg="#212121")
        self.root.geometry("1024x768")
        self.root.resizable(True, True)
        self.root.minsize(width=900, height=675)

    def screenFrames(self):
        self.frame_one = tk.Frame(self.root, bg="#151515", highlightbackground="#555555", highlightthickness=1)
        self.frame_one.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.45)
        
        self.frame_two = tk.Frame(self.root, bg="#151515", highlightbackground="#555555", highlightthickness=1)
        self.frame_two.place(relx=0.05, rely=0.51, relwidth=0.9, relheight=0.45)
    
    def createButtons(self):
        ###Clear Button
        self.button_clear = tk.Button(self.frame_one, text="Clear", bg="#3C3A3A", foreground="white", font=("Calibri", 14, "bold"))
        self.button_clear.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.1)
        
        ###Search Button
        self.button_search = tk.Button(self.frame_one, text="Search", bg="#3C3A3A", foreground="white", font=("Calibri", 14, "bold"))
        self.button_search.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.1)
        
        ###New Button
        self.button_new = tk.Button(self.frame_one, text="New", bg="#3C3A3A", foreground="white", font=("Calibri", 14, "bold"))
        self.button_new.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.1)
        
        ###Change Button
        self.button_change = tk.Button(self.frame_one, text="Change", bg="#3C3A3A", foreground="white", font=("Calibri", 14, "bold"))
        self.button_change.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.1)
        
        ###Change Button
        self.button_change = tk.Button(self.frame_one, text="Erase", bg="#3C3A3A", foreground="white", font=("Calibri", 14, "bold"))
        self.button_change.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.1)
        
        ###Code Entry
        self.label_code = tk.Label(self.frame_one, text="Code", background="#151515", foreground="white", font=("Calibri", 14, "bold"))
        self.label_code.place(relx=0.05, rely=0.05, relwidth=0.07)
        
        self.entry_code = tk.Entry(self.frame_one, background="#3C3A3A", font=("Calibri", 14, "bold"))
        self.entry_code.place(relx=0.05, rely=0.12, relwidth=0.07)
    
Application(root, "TkinterApp")
root.mainloop()

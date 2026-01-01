import tkinter as tk
from tkinter import ttk
import sqlite3

root = tk.Tk()

class ApplicationFunctions:
    def clearScreen(self):
        self.entry_code.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
    
    def connectDatabase(self):
        self.connect = sqlite3.connect("clients.db")

class Application(ApplicationFunctions):
    def __init__(self, root, name):
        
        self.root = root
        self.name = name
        
        self.screen(self.name)
        self.screenFrames()
        self.createButtonsFrameOne()
        self.createListFrameTwo()

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
    
    def createButtonsFrameOne(self):
        ###Clear Button
        self.button_clear = tk.Button(self.frame_one, text="Clear", bg="#3C3A3A", foreground="white", font=("Calibri", 14, "bold"), bd=0, command=self.clearScreen)
        self.button_clear.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.1)
        
        ###Search Button
        self.button_search = tk.Button(self.frame_one, text="Search", bg="#3C3A3A", foreground="white", font=("Calibri", 14, "bold"), bd=0)
        self.button_search.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.1)
        
        ###New Button
        self.button_new = tk.Button(self.frame_one, text="New", bg="#3C3A3A", foreground="white", font=("Calibri", 14, "bold"), bd=0)
        self.button_new.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.1)
        
        ###Change Button
        self.button_change = tk.Button(self.frame_one, text="Change", bg="#3C3A3A", foreground="white", font=("Calibri", 14, "bold"), bd=0)
        self.button_change.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.1)
        
        ###Change Button
        self.button_change = tk.Button(self.frame_one, text="Erase", bg="#3C3A3A", foreground="white", font=("Calibri", 14, "bold"), bd=0)
        self.button_change.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.1)
        
        ###Code Entry
        self.label_code = tk.Label(self.frame_one, text="Code", background="#151515", foreground="white", font=("Calibri", 14, "bold"), bd=0)
        self.label_code.place(relx=0.05, rely=0.05, relwidth=0.07)
        
        self.entry_code = tk.Entry(self.frame_one, background="#3C3A3A", font=("Calibri", 14, "bold"), bd=0)
        self.entry_code.place(relx=0.05, rely=0.12, relwidth=0.07)
        
        ###Name Entry
        self.label_name = tk.Label(self.frame_one, text="Name", background="#151515", foreground="white", font=("Calibri", 14, "bold"), bd=0)
        self.label_name.place(relx=0.0412, rely=0.29, relwidth=0.07)
        
        self.entry_name = tk.Entry(self.frame_one, background="#3C3A3A", font=("Calibri", 14, "bold"), bd=0)
        self.entry_name.place(relx=0.05, rely=0.36, relwidth=0.8, relheight=0.08)
    
    def createListFrameTwo(self):
        self.listCli = ttk.Treeview(self.frame_two, height=3, columns=("col1", "col2", "col3", "col4"))
        self.listCli.heading("#0", text="")
        self.listCli.heading("#1", text="Code")
        self.listCli.heading("#2", text="Name")
        self.listCli.heading("#3", text="Phone")
        self.listCli.heading("#4", text="City")
        
        self.listCli.column("#0", width=1, stretch="No")
        self.listCli.column("#1", width=50)
        self.listCli.column("#2", width=200)
        self.listCli.column("#3", width=125)
        self.listCli.column("#4", width=125)
        
        self.listCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)
        
        self.listScroll = ttk.Scrollbar(self.frame_two, orient="vertical")
        self.listCli.config(yscroll=self.listScroll.set)
        self.listScroll.place(relx=0.96, rely=0.1, relwidth=0.05, relheight=0.85)
    
Application(root, "TkinterApp")
root.mainloop()

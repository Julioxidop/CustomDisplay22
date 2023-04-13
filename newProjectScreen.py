import customtkinter as tk
from Project import Project
from helper import saveProject
from projectScreen import ProjectScreen
import os

class NewProjectScreen(tk.CTkToplevel):
    def __init__(self, master: tk.CTk):
        super().__init__(master)
        self.geometry("250x100")
        self.title("New Project")
        self.label = tk.CTkLabel(self, text="New Project Name")
        self.label.pack()
        self.entry = tk.CTkEntry(self)
        self.entry.pack()

        def createProject():
            name = self.entry.get()
            try:
                os.mkdir(f"./projects/{name}")
            except Exception:
                pass
            new = Project(name)
            saveProject(f"{name}.cd22", new)
            ProjectScreen(master,new,True)
            
            self.destroy()

        self.button = tk.CTkButton(self, text="Create", command= lambda: createProject())
        self.button.pack(pady=5)
        self.geometry("+%d+%d" %(master.winfo_x(),master.winfo_y()+50))
        master.withdraw()

        def on_closing():
            master.deiconify()
            self.destroy()

        self.protocol("WM_DELETE_WINDOW", on_closing)
            

    
import tkinter as tk
from tkinter import ttk
from prelaunch_checks import prelaunch_check, check_api_keys, check_environment
from api_key_manager import save_api_keys, validate_api_keys

class AIApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        print("Initializing AI Agent Application...")
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("AI Agent Application")

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (PrelaunchCheckPage, ModelSelectionPage, AgentConstructionPage):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(PrelaunchCheckPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        self.update_idletasks()
        self.geometry("{}x{}".format(frame.winfo_reqwidth(), frame.winfo_reqheight()))

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Prelaunch Check")
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Next",
        command=lambda: controller.show_frame(ModelSelectionPage))
        button.pack()

class ModelSelectionPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Model Selection")
        label.pack(pady=10, padx=10)

        self.model_var = tk.StringVar()
        model_dropdown = ttk.Combobox(self, textvariable=self.model_var)
        model_dropdown["values"] = (
            "gpt-3.5-turbo",
            "gpt-4",
            "gpt-4-0314",
            "gpt-4-32k",
            "gpt-4-32k-0314"
        )
        model_dropdown.pack(pady=10)

        button = ttk.Button(self, text="Select Model",
                            command=lambda: controller.show_frame(AgentConstructionPage))
        button.pack()

class AgentConstructionPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Agent Construction")
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Exit", command=controller.quit)
        button.pack()

class PrelaunchCheckPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.label = ttk.Label(self, text="Prelaunch Check")
        self.label.pack(pady=10, padx=10)

        self.openai_api_key_label = ttk.Label(self, text="OpenAI API Key:")
        self.openai_api_key_label.pack()
        self.openai_api_key_entry = ttk.Entry(self)
        self.openai_api_key_entry.pack()

        self.google_api_key_label = ttk.Label(self, text="Google API Key:")
        self.google_api_key_label.pack()
        self.google_api_key_entry = ttk.Entry(self)
        self.google_api_key_entry.pack()

        self.error_label = ttk.Label(self, text="", foreground="red")
        self.error_label.pack(pady=10, padx=10)

        self.submit_button = ttk.Button(self, text="Submit API Keys", command=self.submit_api_keys)
        self.submit_button.pack(pady=10)

        self.button = ttk.Button(self, text="Start Prelaunch Check", command=self.retry_prelaunch_check)
        self.button.pack()

    def submit_api_keys(self):
        openai_api_key = self.openai_api_key_entry.get().strip()
        google_api_key = self.google_api_key_entry.get().strip()

        if not validate_api_keys(openai_api_key, google_api_key):
            self.error_label.config(text="Both API keys are required.")
            return

        try:
            save_api_keys(openai_api_key, google_api_key)
            self.error_label.config(text="API keys saved successfully.", foreground="green")
        except Exception as e:
            self.error_label.config(text=str(e), foreground="red")
            
    def retry_prelaunch_check(self):
        try:
            check_api_keys()
            check_environment()
            self.controller.show_frame(ModelSelectionPage)
        except RuntimeError as e:
            self.error_label.config(text=str(e), foreground="red")

                       
def launch_gui():
    app = AIApp()
    app.mainloop()

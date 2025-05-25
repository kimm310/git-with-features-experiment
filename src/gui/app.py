import tkinter as tk
from tkinter import messagebox
from src.calculator.basic import add, subtract
from src.calculator.scientific import power, log
from src.calculator.utils import validate_number

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI Calculator")

        # Inputs
        self.entry1 = tk.Entry(root)
        self.entry1.grid(row=0, column=1, padx=10, pady=10)

        self.entry2 = tk.Entry(root)
        self.entry2.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(root, text="Input 1:").grid(row=0, column=0)
        tk.Label(root, text="Input 2:").grid(row=1, column=0)

        # Result Display
        self.result_var = tk.StringVar()
        tk.Label(root, text="Result:").grid(row=2, column=0)
        self.result_label = tk.Label(root, textvariable=self.result_var, fg="blue")
        self.result_label.grid(row=2, column=1)

        # Operation Buttons
        operations = [
            ("Add", self.handle_add),
            ("Subtract", self.handle_subtract),
            ("Power", self.handle_power),
            ("Log", self.handle_log),
            ("Show History", self.show_history),
        ]

        for i, (name, func) in enumerate(operations):
            btn = tk.Button(root, text=name, command=func)
            btn.grid(row=3 + i // 2, column=i % 2, padx=5, pady=5, sticky='ew')

    def get_inputs(self, require_second=True):
        try:
            a = validate_number(self.entry1.get())
            b = validate_number(self.entry2.get()) if require_second else None
            return a, b
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
            return None, None

    def display_result(self, result):
        self.result_var.set(str(result))
        save_result(result)

    def handle_add(self):
        a, b = self.get_inputs()
        if a is not None:
            self.display_result(add(a, b))

    def handle_subtract(self):
        a, b = self.get_inputs()
        if a is not None:
            self.display_result(subtract(a, b))

    def handle_power(self):
        a, b = self.get_inputs()
        if a is not None:
            self.display_result(modulo(a, b))

    def handle_log(self):
        a, b = self.get_inputs()
        if a is not None:
            self.display_result(log(a, b))
    
    def show_history(self):
        history = get_history()
        messagebox.showinfo("History", "\n".join(str(r) for r in history) if history else "No history available.")
        

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop() 

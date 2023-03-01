import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("NintenBlocks Calculator v1.0")
        master.geometry("320x120")
        root.resizable(False, False)
        master.configure(bg="lightyellow")

        self.label = tk.Label(master, text="Enter file size in MBs:", bg="lightyellow")
        self.label.pack(pady=10)

        self.size_entry = tk.Entry(master, width=10)
        self.size_entry.pack(pady=10)

        self.calculate_button = tk.Button(master, text="Calculate to Blocks", command=self.calculate_blocks)
        self.calculate_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.blocks_label = tk.Label(master, text="Blocks: 0", bg="lightyellow")
        self.blocks_label.pack(side=tk.RIGHT, padx=10, pady=10)

    def calculate_blocks(self):
        size_in_mbs = float(self.size_entry.get())
        size_in_blocks = int(size_in_mbs * 8)
        self.blocks_label.config(text=f"Blocks: {size_in_blocks}")

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()

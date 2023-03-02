import os
import math
import tkinter as tk
from tkinter import filedialog

class NintenBlocksCalculator:
    def __init__(self, master):
        self.master = master
        master.title("NintenBlocks Calculator v2.0")
        master.geometry("520x150")
        master.resizable(False, False)
        master.config(bg='light yellow')

        # Add label for ROM file selection
        self.rom_label = tk.Label(master, text="Select a ROM file:", font=('Arial', 12), bg='light yellow')
        self.rom_label.grid(row=0, column=0, pady=10, padx=10, sticky='w')

        # Add text field for displaying selected ROM file path
        self.rom_file_path = tk.StringVar()
        self.rom_path_textbox = tk.Entry(master, textvariable=self.rom_file_path, width=50, font=('Arial', 10))
        self.rom_path_textbox.grid(row=1, column=0, pady=5, padx=10, sticky='w')

        # Add button for browsing ROM file
        self.browse_button = tk.Button(master, text="Browse", command=self.browse_rom, font=('Arial', 10))
        self.browse_button.grid(row=1, column=1, pady=5, padx=10, sticky='e')

        # Add button for calculating blocks
        self.calculate_button = tk.Button(master, text="Calculate to Blocks", command=self.calculate_blocks, font=('Arial', 12))
        self.calculate_button.grid(row=2, column=0, pady=20, padx=10, sticky='w')

        # Add label for displaying the calculated blocks
        self.blocks_label = tk.Label(master, text="Blocks: 0", font=('Arial', 12), bg='light yellow')
        self.blocks_label.grid(row=2, column=1, pady=20, padx=10, sticky='e')


    def browse_rom(self):
        rom_file_types = [
            ("Nintendo ROMs", "*.cia;*.gba;*.nds;*.sfc"),
            ("All Files", "*.*")
        ]
        rom_file_path = filedialog.askopenfilename(initialdir="/", title="Select ROM File", filetypes=rom_file_types)
        self.rom_path_textbox.delete(0, tk.END)
        self.rom_path_textbox.insert(0, rom_file_path)

    def calculate_blocks(self):
        rom_file_path = self.rom_path_textbox.get()
        if not rom_file_path:
            return

        size_in_bytes = os.path.getsize(rom_file_path)
        size_in_mbs = size_in_bytes / (1024 * 1024)
        blocks = int(math.ceil(size_in_mbs * 8))

        self.blocks_label.config(text=f"Blocks: {blocks}")

root = tk.Tk()
ninten_blocks_calculator = NintenBlocksCalculator(root)
root.mainloop()

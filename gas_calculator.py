import tkinter as tk
from tkinter import messagebox

# Constants
HEATING_VALUE = 38.6  # MJ/m³ (typical)
CORRECTION_FACTOR = 1.013  # default
DEFAULT_COST_PER_MJ = 0.03784  # Optional

def calculate_mj():
    try:
        previous = float(prev_entry.get())
        current = float(curr_entry.get())
        cost_per_mj = float(cost_entry.get())

        volume_used = current - previous
        mj_used = volume_used * HEATING_VALUE * CORRECTION_FACTOR
        cost = mj_used * cost_per_mj

        result_label.config(
            text=f"Gas Used: {volume_used:.2f} m³\n"
                 f"MJ Used: {mj_used:.2f} MJ\n"
                 f"Estimated Cost: ${cost:.2f}"
        )

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# GUI Setup
root = tk.Tk()
root.title("Gas Usage Calculator")

tk.Label(root, text="Previous Reading:").grid(row=0, column=0)
prev_entry = tk.Entry(root)
prev_entry.grid(row=0, column=1)

tk.Label(root, text="Current Reading:").grid(row=1, column=0)
curr_entry = tk.Entry(root)
curr_entry.grid(row=1, column=1)

tk.Label(root, text="Cost per MJ (e.g. 0.03784):").grid(row=2, column=0)
cost_entry = tk.Entry(root)
cost_entry.insert(0, str(DEFAULT_COST_PER_MJ))
cost_entry.grid(row=2, column=1)

tk.Button(root, text="Calculate", command=calculate_mj).grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="", justify="left")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()

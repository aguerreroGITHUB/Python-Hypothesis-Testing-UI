import tkinter as tk
from tkinter import messagebox
import subprocess

# Create the main window
root = tk.Tk()
root.title("Hypothesis Testing UI")
root.geometry("300x100")

# Create a function for the A/B-TEST button
def run_ab_test():
    # Open the ABtest.py script in a pop-up window
    subprocess.call(['python', 'ABtest.py'])

# Create a function for the Z-TEST button
def run_z_test():
    # Open the Ztest.py script in a pop-up window
    subprocess.call(['python', 'Ztest.py'])

# Create a function for the T-TEST button
def run_t_test():
    # Open the Ttest.py script in a pop-up window
    subprocess.call(['python', 'Ttest.py'])

# Create the A/B-TEST button
ab_button = tk.Button(root, text='A/B-TEST', command=run_ab_test)
ab_button.pack()

# Create the Z-TEST button
z_button = tk.Button(root, text='Z-TEST', command=run_z_test)
z_button.pack()

# Create the T-TEST button
t_button = tk.Button(root, text='T-TEST', command=run_t_test)
t_button.pack()

# Add a footer with the text "by Antonio Guerrero"
footer = tk.Label(root, text='©by Antonio Guerrero')
footer.place(relx=1.0, rely=1.0, anchor='se')


# Start the main event loop
root.mainloop()

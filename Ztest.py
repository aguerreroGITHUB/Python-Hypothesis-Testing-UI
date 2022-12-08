import tkinter as tk
import sys
sys.argv = ['Ztest.py']

# Create a new Tkinter window
window = tk.Tk()
window.title("Z-Test")

# Define a function that calculates the Z-score
# based on the given input values
def calculate_zscore(mean, pop_mean, std, sample_size):
  if std == 0 or sample_size == 0:
    return "Invalid input: standard deviation and sample size must be non-zero values"
  else:
    z_score = (mean - pop_mean) / (std / (sample_size**0.5))
  return z_score

# Create labels, entry fields, and a button to allow the user
# to input the necessary values and calculate the Z-score

pop_mean_label = tk.Label(window, text="Population Mean:")
pop_mean_label.grid(row=0, column=0)
pop_mean_field = tk.Entry(window)
pop_mean_field.grid(row=0, column=1)

mean_label = tk.Label(window, text="Sample Mean:")
mean_label.grid(row=1, column=0)
mean_field = tk.Entry(window)
mean_field.grid(row=1, column=1)

std_label = tk.Label(window, text="Sample Standard Deviation:")
std_label.grid(row=2, column=0)
std_field = tk.Entry(window)
std_field.grid(row=2, column=1)

sample_size_label = tk.Label(window, text="Sample Size:")
sample_size_label.grid(row=3, column=0)
sample_size_field = tk.Entry(window)
sample_size_field.grid(row=3, column=1)

calc_button = tk.Button(window, text="Calculate Z-Score", command=lambda: z_score_label.config(text="Z Score: %.2f" % calculate_zscore(float(mean_field.get()),
  float(pop_mean_field.get()),
  float(std_field.get()),
  float(sample_size_field.get()))))
calc_button.grid(row=4, column=0, columnspan=2)

# Create a new label to display the Z Score
z_score_label = tk.Label(window, text="Z Score:")
z_score_label.place(relx=0.5, rely=0.95, anchor="center")

# Blank labels
blank_label = tk.Label(window, text=" ")
blank_label.grid(row=5, column=0)


# Display the Tkinter window
window.mainloop()